from datetime import datetime

def calculate_years_difference(date_str1, date_str2):
    date_format = "%Y-%m-%d"
    try:
        date1 = datetime.strptime(date_str1, date_format)
        date2 = datetime.strptime(date_str2, date_format)
    except ValueError as e:
        raise ValueError("Invalid date format. Please use YYYY-MM-DD.") from e
    
    years_difference = abs((date2 - date1).days) // 365
    return years_difference

if __name__ == '__main__':
    sample_date1 = "1990-05-15"
    sample_date2 = "2023-04-10"
    print(calculate_years_difference(sample_date1, sample_date2))