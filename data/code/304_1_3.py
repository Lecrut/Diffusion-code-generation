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
        invalid_date = "not-a-date"
        result = is_earlier(date_a, invalid_date)
        print(f"Is {date_a} earlier than '{invalid_date}'? {result}")
    except Exception as e:
        print(f"An unexpected error occurred during comparison with invalid input: {e}")