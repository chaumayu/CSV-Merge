import pandas as pd

df = pd.read_excel('Data/SWS1014_F.xlsx')
print df.shape
df1 = pd.read_excel('Data/SWS1014_S.xlsx')
print df1.shape

print df.shape[0] + df1.shape[0]

merge_df = df.append(df1, ignore_index=True)
print merge_df.shape

merge_df.to_csv('Results/SWS1014.csv', index=False)

df2 = pd.read_csv('Results/SWS1014.csv')
print df2.shape

'''
SWS0713

881259, 4)
(612095, 4)
1493354
(1493354, 4)
(1493354, 4)

SWS1014

(840902, 4)
(558448, 4)
1399350
(1399350, 4)
(1399350, 4)
'''
