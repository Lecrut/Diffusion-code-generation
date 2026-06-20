from datetime import datetime

def validate_date(date_str: str) -> bool:
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def calculate_year_difference(date1_str: str, date2_str: str) -> int:
    if not (validate_date(date1_str) and validate_date(date2_str)):
        raise ValueError("Invalid date format. Please use YYYY-MM-DD.")
    
    date1 = datetime.strptime(date1_str, "%Y-%m-%d")
    date2 = datetime.strptime(date2_str, "%Y-%m-%d")
    return abs((date2.year - date1.year))

if __name__ == '__main__':
    date1 = "2000-05-15"
    date2 = "2023-08-20"
    difference = calculate_year_difference(date1, date2)
    print(difference)