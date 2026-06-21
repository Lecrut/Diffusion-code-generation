from datetime import datetime

def compute_year_difference(date1_str: str, date2_str: str) -> int:
    try:
        date1 = datetime.strptime(date1_str, "%Y-%m-%d")
        date2 = datetime.strptime(date2_str, "%Y-%m-%d")
    except ValueError as e:
        raise ValueError(f"Invalid date format. Expected YYYY-MM-DD. Error: {e}")

    return abs(date1.year - date2.year)

if __name__ == '__main__':
    result = compute_year_difference("2020-01-01", "2023-12-31")
    print(result)