import datetime
def is_earlier(date1: datetime.date, date2: datetime.date) -> bool:
    try:
        return date1 < date2
    except TypeError:
        return False
if __name__ == '__main__':
    date_a = datetime.date(2023, 1, 15)
    date_b = datetime.date(2023, 1, 20)
    date_c = datetime.date(2023, 1, 15)
    print(f"Is {date_a} earlier than {date_b}? {is_earlier(date_a, date_b)}")
    print(f"Is {date_b} earlier than {date_a}? {is_earlier(date_b, date_a)}")
    print(f"Is {date_a} earlier than {date_c}? {is_earlier(date_a, date_c)}")
    print(f"Is {date_c} earlier than {date_a}? {is_earlier(date_c, date_a)}")
    try:
        is_earlier(datetime.date(2023, 1, 1), "not_a_date")
    except Exception:
        pass