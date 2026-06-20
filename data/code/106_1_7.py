from datetime import datetime

def calculate_year_difference(date_str1, date_str2):
    try:
        date_format = "%Y-%m-%d"
        date1 = datetime.strptime(date_str1, date_format)
        date2 = datetime.strptime(date_str2, date_format)
        return abs((date1.year - date2.year))
    except ValueError as e:
        raise ValueError("Invalid date format. Please use YYYY-MM-DD.") from e

if __name__ == '__main__':
    print(calculate_year_difference("2023-04-15", "1990-07-20"))
    print(calculate_year_difference("2000-01-01", "2024-12-31"))
    print(calculate_year_difference("1850-05-05", "1900-11-11"))