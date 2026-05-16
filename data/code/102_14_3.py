import datetime
def is_weekday(date_string):
    try:
        date_obj = datetime.datetime.strptime(date_string, '%m/%d/%Y')
        weekday = date_obj.weekday()
        return 0 <= weekday <= 4
    except ValueError:
        return False
if __name__ == '__main__':
    date1 = "01/01/2024"
    date2 = "02/15/2024"
    date3 = "03/10/2024"
    date4 = "04/20/2024"
    date5 = "05/01/2024"
    print(f"{date1}: {is_weekday(date1)}")
    print(f"{date2}: {is_weekday(date2)}")
    print(f"{date3}: {is_weekday(date3)}")
    print(f"{date4}: {is_weekday(date4)}")
    print(f"{date5}: {is_weekday(date5)}")