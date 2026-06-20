import datetime

def calculate_date_difference(date_str1, date_str2):
    try:
        date1 = datetime.datetime.strptime(date_str1, '%Y-%m-%d')
        date2 = datetime.datetime.strptime(date_str2, '%Y-%m-%d')
        difference = abs((date2 - date1).days)
        weeks = difference / 7
        return weeks
    except ValueError:
        raise ValueError("Error: Invalid date format. Please use YYYY-MM-DD.")

if __name__ == '__main__':
    try:
        result = calculate_date_difference("2023-01-15", "2023-03-20")
        print(result)
    except ValueError as e:
        print(e)