from datetime import date, timedelta

def difference_in_weeks(date_str1, date_str2):
    try:
        date1 = date.strptime(date_str1, '%Y-%m-%d')
        date2 = date.strptime(date_str2, '%Y-%m-%d')
        time_difference = abs(date1 - date2)
        weeks = time_difference.days / 7
        return int(weeks)
    except ValueError:
        raise ValueError("Invalid date format. Please use YYYY-MM-DD.")

if __name__ == '__main__':
    try:
        diff_ab = difference_in_weeks('2023-01-01', '2023-01-29')
        print(f"Difference between 2023-01-01 and 2023-01-29: {diff_ab} weeks")
        
        diff_bc = difference_in_weeks('2023-07-01', '2024-01-01')
        print(f"Difference between 2023-07-01 and 2024-01-01: {diff_bc} weeks")
        
        diff_ac = difference_in_weeks('2023-01-01', '2023-07-01')
        print(f"Difference between 2023-01-01 and 2023-07-01: {diff_ac} weeks")
    except ValueError as e:
        print(e)