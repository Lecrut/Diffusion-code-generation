import datetime

def is_weekday(date_string):
    try:
        date_obj = datetime.datetime.strptime(date_string, '%Y-%m-%d')
        return date_obj.weekday() < 5
    except ValueError:
        return False

if __name__ == '__main__':
    date1 = "2023-10-25"
    date2 = "2023-10-26"
    date3 = "2023-10-27"
    date4 = "2023-10-28"
    date_invalid = "2023/10/25"
    print(f"Is {date1} a weekday? {is_weekday(date1)}")
    print(f"Is {date2} a weekday? {is_weekday(date2)}")
    print(f"Is {date3} a weekday? {is_weekday(date3)}")
    print(f"Is {date4} a weekday? {is_weekday(date4)}")
    print(f"Is {date_invalid} a weekday? {is_weekday(date_invalid)}")