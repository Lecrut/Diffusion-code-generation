from datetime import datetime

def compute_year_difference(date1_str: str, date2_str: str) -> int:
    try:
        date1 = datetime.strptime(date1_str, "%Y-%m-%d")
        date2 = datetime.strptime(date2_str, "%Y-%m-%d")
    except ValueError as e:
        raise ValueError(f"Invalid date format. Expected YYYY-MM-DD. Error: {e}")
    
    diff = date2 - date1
    days = diff.days
    years = days // 365
    return years

if __name__ == '__main__':
    result = compute_year_difference("2020-01-01", "2025-01-01")
    print(result)