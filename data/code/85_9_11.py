import datetime

def calculate_week_difference(date_str1, date_str2):
    try:
        date1 = datetime.datetime.strptime(date_str1, '%Y-%m-%d').date()
        date2 = datetime.datetime.strptime(date_str2, '%Y-%m-%d').date()
        delta = abs((date1 - date2).days)
        weeks = delta // 7
        return weeks
    except ValueError:
        raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.")

if __name__ == '__main__':
    try:
        result1 = calculate_week_difference('2023-01-01', '2023-01-10')
        print(f"Difference between 2023-01-01 and 2023-01-10: {result1} weeks")
        
        result2 = calculate_week_difference('2023-01-10', '2022-01-01')
        print(f"Difference between 2023-01-10 and 2022-01-01: {result2} weeks")
        
        result3 = calculate_week_difference('2024-05-01', '2024-04-01')
        print(f"Difference between 2024-05-01 and 2024-04-01: {result3} weeks")
    except ValueError as e:
        print(e)