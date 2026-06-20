from datetime import datetime

def calculate_difference(date_str1, date_str2):
    try:
        date_format = "%m/%d/%Y"
        date1 = datetime.strptime(date_str1, date_format)
        date2 = datetime.strptime(date_str2, date_format)
        return abs((date2 - date1).days)
    except ValueError as e:
        raise ValueError("Invalid date format. Please use MM/DD/YYYY.") from e

if __name__ == '__main__':
    try:
        difference = calculate_difference('01/01/2023', '01/10/2023')
        print(difference)
    except ValueError as e:
        print(e)