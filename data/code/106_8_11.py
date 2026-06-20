from datetime import datetime

def calculate_year_difference(date_str1, date_str2):
    try:
        date1 = datetime.strptime(date_str1, "%Y-%m-%d")
        date2 = datetime.strptime(date_str2, "%Y-%m-%d")
        return abs((date2 - date1).days // 365)
    except ValueError as e:
        raise ValueError("Invalid date format. Please use YYYY-MM-DD.") from e

if __name__ == '__main__':
    date1 = "2000-01-01"
    date2 = "1995-01-01"
    difference = calculate_year_difference(date1, date2)
    print(difference)