import pandas as pd
from os import listdir
from os.path import isfile, join


# mypath = 'data/Инвестиции/'
# onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
# print(onlyfiles)
# for i in range(len(onlyfiles)):
#     print(i, onlyfiles[i])

# df = pd.ExcelFile(mypath + onlyfiles[0])

# sheet_names = df.sheet_names  # see all sheet names
# # print(sheet_names)

# df_file_1 = pd.read_excel(df, sheet_names[0], skiprows=2) 
# column_names = list(df_file_1.columns)
# df_file_1.rename(columns={df_file_1.columns[0]: 'Countries'}, inplace=True)
# print(df_file_1)


# df = pd.ExcelFile(mypath + onlyfiles[1])
# sheet_names = df.sheet_names  # see all sheet names
# print(onlyfiles[1], sheet_names)

# df_file_2 = pd.read_excel(df, '2', skiprows=3) 
# print(df_file_2)
# column_names = list(df_file_2.columns)
# column_names[0] = 'Countries'
# df_file_2 = pd.DataFrame(df_file_2, columns=column_names)
# print(df_file_2)

# for i in onlyfiles:
#     if i == 'Инвестиции в основной капитал по направлениям использования (2003-2023).xlsx':
#         df = pd.ExcelFile(mypath + i)

#         sheet_names = df.sheet_names  # see all sheet names

#         df_file_2 = pd.read_excel(df, sheet_names[0], skiprows=2) 
#         column_names = list(df_file_2.columns)
#         df_file_2.rename(columns={df_file_2.columns[0]: 'Industry'}, inplace=True)
#         df_file_2 = df_file_2.drop([df_file_2.index[1], df_file_2.index[-1]])

#         print(df_file_2)

#     if i == 'Б-06-01-М (08 2024) рус.xlsx':
#         df = pd.ExcelFile(mypath + i)

#         sheet_names = df.sheet_names  # see all sheet names

#         df_file_3 = pd.read_excel(df, '5', skiprows=3) 
#         column_names = list(df_file_3.columns)
#         print(df_file_3)
#         df_file_3 = df_file_3.drop([df_file_3.index[1]])

#         print(df_file_3)


# df = pandas


# mypath = 'data/Структурная статистика/'
# onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
# # for i in range(len(onlyfiles)):
# #     print(i, onlyfiles[i])

# for i in onlyfiles:
#     if i == 'Б-16-01 1- ПФ (1 2024)русс.xlsx':
#         m = ['2 ', '5 ', '6', '7', '8', '43', '44']
#         d = {}
#         df = pd.ExcelFile(mypath + i)
#         for page in m:
#             if page in ('2 ', '43', '44'):
#                 df_file = pd.read_excel(df, page, skiprows=3) 
                
#                 if page in ('2 ', '44'):
#                     df_file.rename(columns={df_file.columns[0]: 'Industry'}, inplace=True)
#                 elif page == '43':
#                     df_file.rename(columns={df_file.columns[0]: 'Region'}, inplace=True)
#                 print(df_file)
#                 d[page] = df_file
#             elif page in ('5 ', '6'):
#                 df_file = pd.read_excel(df, page, skiprows=4) 
#                 column_names = list(df_file.columns)

#                 if page == '5 ':
#                     df_file.rename(columns={df_file.columns[0]: 'Region'}, inplace=True)
#                 elif page == '6':
#                     df_file.rename(columns={df_file.columns[0]: 'Industry'}, inplace=True)
#                 print(df_file)
#                 d[page] = df_file

#             elif page in ('7', '8'):
#                 df_file = pd.read_excel(df, page, skiprows=5) 
#                 column_names = list(df_file.columns)

#                 if page == '7':
#                     df_file.rename(columns={df_file.columns[0]: 'Region'}, inplace=True)
#                 if page == '8':
#                     df_file.rename(columns={df_file.columns[0]: 'Industry'}, inplace=True)
#                 print(df_file)
#                 d[page] = df_file

# print(d)
            

# mypath = 'data/Информационно-коммуникационные технологии и связь/Затраты на информационно-коммуникационные технологии.xls'
# df_file = pd.read_excel(mypath, 'рус', skiprows=2) 
# df_file.rename(columns={df_file.columns[0]: 'Spendings'}, inplace=True)

# print(df_file)


mypath = 'data/Информационно-коммуникационные технологии и связь/Уровень цифровой грамотности населения.xlsx'
df_file = pd.read_excel(mypath, skiprows=5) 
df_file.rename(columns={df_file.columns[0]: 'Region'}, inplace=True)
print(df_file)


mypath = 'data/Информационно-коммуникационные технологии и связь/Наличие средств связи, число предоставленных услуг.xls'
df_file = pd.read_excel(mypath, skiprows=2) 
df_file.rename(columns={df_file.columns[0]: 'Services'}, inplace=True)
print(df_file)