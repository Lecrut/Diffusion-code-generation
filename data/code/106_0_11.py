from datetime import datetime

def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def calculate_age_difference(date_str1, date_str2):
    if not (is_valid_date(date_str1) and is_valid_date(date_str2)):
        raise ValueError("Inputs must be valid dates in YYYY-MM-DD format.")
    
    date_format = "%Y-%m-%d"
    date1 = datetime.strptime(date_str1, date_format)
    date2 = datetime.strptime(date_str2, date_format)
    age_difference = abs((date2 - date1).days) // 365
    return age_difference

if __name__ == '__main__':
    sample_date1 = "1990-05-15"
    sample_date2 = "2023-04-10"
    print(calculate_age_difference(sample_date1, sample_date2))