from datetime import datetime

def validate_dates(date1, date2):
    if not isinstance(date1, str) or not isinstance(date2, str):
        raise ValueError("Inputs must be strings in the format 'YYYY-MM-DD'.")
    
    try:
        datetime.strptime(date1, "%Y-%m-%d")
        datetime.strptime(date2, "%Y-%m-%d")
    except ValueError as e:
        raise ValueError(f"Invalid date format: {e}")

def calculate_age_difference(date_str1, date_str2):
    validate_dates(date_str1, date_str2)
    date_format = "%Y-%m-%d"
    date1 = datetime.strptime(date_str1, date_format)
    date2 = datetime.strptime(date_str2, date_format)
    age_diff = abs((date2 - date1).days) // 365
    return age_diff

if __name__ == '__main__':
    sample_date1 = "1990-05-15"
    sample_date2 = "2023-04-10"
    print(calculate_age_difference(sample_date1, sample_date2))