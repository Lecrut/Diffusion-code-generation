from datetime import date

weekday_map = {0: True, 1: True, 2: True, 3: True, 4: True}

def is_weekday(date_obj: date) -> bool:
    return weekday_map.get(date_obj.weekday(), False)

if __name__ == '__main__':
    date1 = date(2023, 10, 2)
    date2 = date(2023, 10, 3)
    date3 = date(2023, 10, 6)
    date4 = date(2023, 10, 7)
    date5 = date(2023, 10, 8)

    print(f"Is {date1} a weekday? {is_weekday(date1)}")
    print(f"Is {date2} a weekday? {is_weekday(date2)}")
    print(f"Is {date3} a weekday? {is_weekday(date3)}")
    print(f"Is {date4} a weekday? {is_weekday(date4)}")
    print(f"Is {date5} a weekday? {is_weekday(date5)}")