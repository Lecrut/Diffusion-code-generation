from datetime import date
def is_weekday(date_object):
    return date_object.weekday() < 5
if __name__ == '__main__':
    date1 = date(2023, 10, 23)
    date2 = date(2023, 10, 24)
    date3 = date(2023, 10, 27)
    date4 = date(2023, 10, 28)
    print(f"Is {date1} a weekday? {is_weekday(date1)}")
    print(f"Is {date2} a weekday? {is_weekday(date2)}")
    print(f"Is {date3} a weekday? {is_weekday(date3)}")
    print(f"Is {date4} a weekday? {is_weekday(date4)}")