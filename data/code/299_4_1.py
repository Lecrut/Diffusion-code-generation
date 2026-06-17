import datetime
def is_weekend(date_string):
    try:
        date_obj = datetime.datetime.strptime(date_string, '%m/%d/%Y')
        day_of_week = date_obj.weekday()
        if day_of_week >= 5:
            return True
        else:
            return False
    except ValueError:
        return None
if __name__ == '__main__':
    date1 = "01/01/2024"
    date2 = "01/07/2024"
    date3 = "01/06/2024"
    date4 = "12/25/2023"
    date5 = "99/99/2023"
    print(f"{date1}: {is_weekend(date1)}")
    print(f"{date2}: {is_weekend(date2)}")
    print(f"{date3}: {is_weekend(date3)}")
    print(f"{date4}: {is_weekend(date4)}")
    print(f"{date5}: {is_weekend(date5)}")