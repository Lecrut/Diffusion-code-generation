import datetime
def is_earlier(date1: datetime.date, date2: datetime.date) -> bool:
    try:
        return date1 < date2
    except TypeError:
        return False
if __name__ == '__main__':
    d1 = datetime.date(2023, 1, 15)
    d2 = datetime.date(2023, 1, 20)
    d3 = datetime.date(2023, 1, 15)
    print(f"Is {d1} earlier than {d2}? {is_earlier(d1, d2)}")
    print(f"Is {d2} earlier than {d1}? {is_earlier(d2, d1)}")
    print(f"Is {d1} earlier than {d3}? {is_earlier(d1, d3)}")
    try:
        is_earlier(d1, "not_a_date")
    except Exception:
        pass