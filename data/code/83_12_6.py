from datetime import datetime

def compare_dates(date_str1, date_str2):
    try:
        date1 = datetime.strptime(date_str1, "%Y-%m-%d")
        date2 = datetime.strptime(date_str2, "%Y-%m-%d")
        return date1 == date2
    except ValueError:
        return False

if __name__ == '__main__':
    date_pairs = {
        ("2023-10-27", "2023-10-27"): True,
        ("2023-10-27", "2023-10-28"): False,
        ("2023-10-27", "2023/10/27"): False
    }

    for (date_a, date_b), expected in date_pairs.items():
        result = compare_dates(date_a, date_b)
        print(f"Comparing {date_a} and {date_b}: {result} (Expected: {expected})")