from datetime import datetime

def calculate_difference(date_str1, date_str2):
    try:
        date_format = "%Y-%m-%d"
        date1 = datetime.strptime(date_str1, date_format)
        date2 = datetime.strptime(date_str2, date_format)
        return abs((date2 - date1).days) // 365
    except ValueError:
        raise ValueError("Invalid input. Please enter dates in YYYY-MM-DD format.")

if __name__ == '__main__':
    year1 = '2023-04-10'
    year2 = '1998-07-20'
    try:
        difference = calculate_difference(year1, year2)
        print(difference)
    except ValueError as e:
        print(e)