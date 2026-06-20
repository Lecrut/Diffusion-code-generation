from datetime import datetime

def compare_dates(date_str1, date_str2):
    try:
        date1 = datetime.strptime(date_str1, "%Y-%m-%d")
        date2 = datetime.strptime(date_str2, "%Y-%m-%d")
        return date1 == date2
    except ValueError:
        return False

if __name__ == '__main__':
    date_a = "2023-10-27"
    date_b = "2023-10-28"
    date_c = "2023-10-29"
    print(f"Comparing {date_a} and {date_b}: {compare_dates(date_a, date_b)}")
    print(f"Comparing {date_a} and {date_c}: {compare_dates(date_a, date_c)}")