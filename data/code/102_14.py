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
    date2 = "02/29/2024"
    date3 = "03/15/2024"
    date4 = "12/31/2023"
    date5 = "04/30/2024"
    date6 = "13/01/2024"
    print(f"Is {date1} a weekday? {is_weekday(date1)}")
    print(f"Is {date2} a weekday? {is_weekday(date2)}")
    print(f"Is {date3} a weekday? {is_weekday(date3)}")
    print(f"Is {date4} a weekday? {is_weekday(date4)}")
    print(f"Is {date5} a weekday? {is_weekday(date5)}")
    print(f"Is {date6} a weekday? {is_weekday(date6)}")