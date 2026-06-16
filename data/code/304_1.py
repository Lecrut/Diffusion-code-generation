import datetime
def is_earlier(date1, date2):
    try:
        return date1 < date2
    except TypeError:
        return False
if __name__ == '__main__':
    date_a = datetime.date(2023, 1, 1)
    date_b = datetime.date(2023, 1, 5)
    print(f"Is {date_a} earlier than {date_b}? {is_earlier(date_a, date_b)}")
    date_c = datetime.date(2024, 5, 10)
    date_d = datetime.date(2023, 12, 31)
    print(f"Is {date_c} earlier than {date_d}? {is_earlier(date_c, date_d)}")
    date_e = datetime.date(2025, 1, 1)
    date_f = datetime.date(2024, 1, 1)
    print(f"Is {date_e} earlier than {date_f}? {is_earlier(date_e, date_f)}")
    try:
        invalid_date = "not-a-date"
        result = is_earlier(date_a, invalid_date)
        print(f"Is {date_a} earlier than '{invalid_date}'? {result}")
    except Exception as e:
        print(f"An unexpected error occurred during comparison: {e}")