import datetime
def is_earlier(date1: datetime.date, date2: datetime.date) -> bool:
    try:
        return date1 < date2
    except TypeError:
        return False
if __name__ == '__main__':
    date_a = datetime.date(2023, 1, 1)
    date_b = datetime.date(2023, 1, 5)
    date_c = datetime.date(2022, 12, 31)
    date_d = datetime.date(2023, 1, 1)
    print(f"Is {date_a} earlier than {date_b}? {is_earlier(date_a, date_b)}")
    print(f"Is {date_b} earlier than {date_a}? {is_earlier(date_b, date_a)}")
    print(f"Is {date_c} earlier than {date_a}? {is_earlier(date_c, date_a)}")
    print(f"Is {date_d} earlier than {date_d}? {is_earlier(date_d, date_d)}")
    try:
        invalid_date1 = "not-a-date"
        invalid_date2 = datetime.date(2023, 1, 1)
        print(f"Comparing invalid string '{invalid_date1}' with {invalid_date2}: {is_earlier(invalid_date1, invalid_date2)}")
    except Exception:
        pass