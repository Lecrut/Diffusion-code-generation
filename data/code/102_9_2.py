import datetime
def is_weekday(date_obj: datetime.date) -> bool:
    return date_obj.weekday() < 5
if __name__ == '__main__':
    date1 = datetime.date(2023, 10, 25)
    date2 = datetime.date(2023, 10, 26)
    date3 = datetime.date(2023, 10, 27)
    date4 = datetime.date(2023, 10, 28)
    print(f"Is {date1} a weekday? {is_weekday(date1)}")
    print(f"Is {date2} a weekday? {is_weekday(date2)}")
    print(f"Is {date3} a weekday? {is_weekday(date3)}")
    print(f"Is {date4} a weekday? {is_weekday(date4)}")