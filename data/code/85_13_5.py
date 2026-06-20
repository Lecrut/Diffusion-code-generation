from datetime import datetime

def calculate_week_difference(date_str1: str, date_str2: str) -> int:
    try:
        date_format = '%Y-%m-%d'
        date1 = datetime.strptime(date_str1, date_format)
        date2 = datetime.strptime(date_str2, date_format)
        difference = abs((date2 - date1).days)
        weeks = difference // 7
        return weeks
    except ValueError:
        raise ValueError("Error: Invalid date format. Please use YYYY-MM-DD.")

if __name__ == '__main__':
    try:
        result = calculate_week_difference('2023-01-15', '2023-02-28')
        print(f"The difference between 2023-01-15 and 2023-02-28 is {result} weeks.")
    except ValueError as e:
        print(e)