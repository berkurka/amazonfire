import pandas as pd
import glob

def import_multiple_csv(path, starts_with, column_sep=',',col_name_dic={},col_dtypes_dic={}, date_columns = []):
    """
    Imports all csv files from a folder and stacks them in one data frame.
    path: path to where files are located
    starts_with: beggining of files name
    column_sep: column separator
    col_name_dic: dictionary to rename columns
    col_dtypes_dic: dictionary to change data types
    
    Example: import_multiple_csv('C:/project/'
                                 ,'sales_report'
                                 ,column_sep=','
                                 ,col_name_dic={'Total Sales':'tot_sales'}
                                 ,col_dtypes_dic={'Total Sales':'int64'})
    """  
    #List with file names
    all_files = glob.glob(path + starts_with + "*.csv")
    #Empty list to store multiple Pandas Data Frames
    li = []
    #Import each file and append it to a list
    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0,sep=';', dtype=col_dtypes_dic, parse_dates=date_columns)
        li.append(df)

    # Concatenate all Data Frames from the list
    frame = pd.concat(li, axis=0, ignore_index=True)
    # Renaming columns
    frame.rename(col_name_dic, axis =1, inplace=True)
    return frame