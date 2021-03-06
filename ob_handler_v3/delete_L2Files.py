"""
Delete L2 files from specific dates
Created by Ofek Yankis on 2021-12-16
Last Updated on 2021-12-16
Maintained by Ofek Yankis ofek5202@gmail.com
Description:
This is a application for deleting L2 files from specified time span chosen by the user. (KOLEL!!!)
"""

from datetime import datetime

import _util as util
import _sqlhandler as sql


def UserInput():
    try:
        start_date = datetime.strptime(
            input("Please put the start date from which you want the data, in the following format: YYYY-MM-DD.\nYour answer: "),
            "%Y-%m-%d")
        end_date   = datetime.strptime(
            input("Please put the last date from which you want the data, in the following format: YYYY-MM-DD.\nYour answer: "),
            "%Y-%m-%d")       
    except:
        print("An invalid date was entered.")
        exit("Program terminated.")

    return start_date, end_date, 

def main():
    start_date, end_date = UserInput()  
    
    l2List = util.GetExistingFilenamesAndPaths(params.path_to_data+"L2/")
    location_pointer = 0
    for file in l2List[1]:

        properties = util.GetFileProperties(file)
        if properties["date"] >= start_date and properties["date"] <= end_date:
            sql.DeleteSpecificFile(l2List[0][location_pointer], file)
        location_pointer += 1    
    


if __name__ == "__main__":
    main()
