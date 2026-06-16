import datetime
def check_weekend(date_string):
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
    date1 = '01/01/2024'
    date2 = '01/07/2024'
    date3 = '02/10/2024'
    date4 = '12/25/2023'
    date5 = '30/04/2024'
    print(f"Date: {date1}, Is Weekend: {check_weekend(date1)}")
    print(f"Date: {date2}, Is Weekend: {check_weekend(date2)}")
    print(f"Date: {date3}, Is Weekend: {check_weekend(date3)}")
    print(f"Date: {date4}, Is Weekend: {check_weekend(date4)}")
    print(f"Date: {date5}, Is Weekend: {check_weekend(date5)}")
    invalid_date = '2024-01-01'
    print(f"Date: {invalid_date}, Is Weekend: {check_weekend(invalid_date)}")