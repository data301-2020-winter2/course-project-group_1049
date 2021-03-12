import pandas as pd

def load_and_process(url):
    df=(
        pd.read_csv(
            url
            #usecols=["victory_status","winner","white_id","white_rating","black_id","black_rating","opening_name"]
        )
    )
    
    for ind, row in df.iterrows():
        list1=row['moves'].split(' ')
        if(len(list1)>0):
            df.loc[ind, "first_move_white"]=list1[0]
            if(len(list1)>1):
                df.loc[ind, "first_move_black"]=list1[1]
    
    df=df.drop(['id', 'created_at', 'last_move_at', 'increment_code', 'moves', 'opening_eco', 'opening_ply'],axis=1)
    df=df.sort_values(by=['rated', 'white_id', 'black_id'], ascending=True)
    
    return df