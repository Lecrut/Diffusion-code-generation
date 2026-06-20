from datetime import datetime

def calculate_year_difference(date_str1, date_str2):
    try:
        date_format = "%Y-%m-%d"
        date1 = datetime.strptime(date_str1, date_format)
        date2 = datetime.strptime(date_str2, date_format)
        return abs((date2 - date1).days // 365)
    except ValueError:
        raise ValueError("Invalid date format. Please use YYYY-MM-DD.")

if __name__ == '__main__':
    date1 = "2000-01-01"
    date2 = "2020-12-31"
    difference = calculate_year_difference(date1, date2)
    print(difference)