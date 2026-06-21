from datetime import datetime

def compute_year_difference(date1_str: str, date2_str: str) -> int:
    if not isinstance(date1_str, str) or not isinstance(date2_str, str):
        raise TypeError("Inputs must be strings")
    try:
        date1 = datetime.strptime(date1_str, "%Y-%m-%d")
        date2 = datetime.strptime(date2_str, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid date format. Expected YYYY-MM-DD.")
    years_diff = date2.year - date1.year
    if (date2.month, date2.day) < (date1.month, date1.day):
        years_diff -= 1
    return abs(years_diff)

if __name__ == '__main__':
    result = compute_year_difference("2020-02-28", "2023-03-01")
    print(result)