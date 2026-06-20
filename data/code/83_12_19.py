from datetime import datetime

def dates_are_equal(date_str1: str, date_str2: str) -> bool:
    try:
        DATE_FORMAT = "%Y-%m-%d"
        date1 = datetime.strptime(date_str1, DATE_FORMAT)
        date2 = datetime.strptime(date_str2, DATE_FORMAT)
        return date1 == date2
    except ValueError:
        return False

if __name__ == '__main__':
    date_a = "2023-10-27"
    date_b = "2023-10-27"
    date_c = "2023-10-28"
    date_d = "2023/10/27"

    print(f"Comparing {date_a} and {date_b}: {dates_are_equal(date_a, date_b)}")
    print(f"Comparing {date_a} and {date_c}: {dates_are_equal(date_a, date_c)}")
    print(f"Comparing {date_a} and {date_d}: {dates_are_equal(date_a, date_d)}")