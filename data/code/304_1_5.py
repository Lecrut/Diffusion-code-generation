import datetime
def is_earlier(date1: datetime.date, date2: datetime.date) -> bool:
    try:
        return date1 < date2
    except TypeError:
        return False
if __name__ == '__main__':
    date_a = datetime.date(2023, 1, 1)
    date_b = datetime.date(2023, 1, 5)
    print(f"Is {date_a} earlier than {date_b}? {is_earlier(date_a, date_b)}")
    date_c = datetime.date(2023, 1, 10)
    date_d = datetime.date(2023, 1, 1)
    print(f"Is {date_c} earlier than {date_d}? {is_earlier(date_c, date_d)}")
    date_e = datetime.date(2024, 5, 1)
    date_f = datetime.date(2023, 12, 31)
    print(f"Is {date_e} earlier than {date_f}? {is_earlier(date_e, date_f)}")
    try:
        is_earlier(datetime.date(2023, 1, 1), "not_a_date")
    except Exception as e:
        print(f"Error caught during comparison: {e}")