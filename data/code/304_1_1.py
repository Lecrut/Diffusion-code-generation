import datetime
def compare_dates(date1, date2):
    try:
        return date1 < date2
    except TypeError:
        return False
if __name__ == '__main__':
    date_a = datetime.date(2023, 1, 1)
    date_b = datetime.date(2023, 1, 5)
    print(f"Is {date_a} earlier than {date_b}? {compare_dates(date_a, date_b)}")
    date_c = datetime.date(2024, 5, 10)
    date_d = datetime.date(2024, 1, 1)
    print(f"Is {date_c} earlier than {date_d}? {compare_dates(date_c, date_d)}")
    date_e = datetime.date(2023, 12, 31)
    date_f = datetime.date(2023, 12, 31)
    print(f"Is {date_e} earlier than {date_f}? {compare_dates(date_e, date_f)}")
    try:
        invalid_date = "not-a-date"
        result = compare_dates(date_a, invalid_date)
        print(f"Comparing valid date with invalid string: {result}")
    except Exception as e:
        print(f"Caught unexpected error during comparison: {e}")