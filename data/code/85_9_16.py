import datetime

def calculate_week_difference(date1_str, date2_str):
    date_format = "%Y-%m-%d"
    date1 = datetime.datetime.strptime(date1_str, date_format).date()
    date2 = datetime.datetime.strptime(date2_str, date_format).date()
    delta = abs(date1 - date2)
    weeks = delta.days // 7
    return weeks

if __name__ == '__main__':
    result1 = calculate_week_difference('2023-01-01', '2023-01-10')
    print(f"Difference between 2023-01-01 and 2023-01-10: {result1} weeks")
    result2 = calculate_week_difference('2023-01-10', '2022-01-01')
    print(f"Difference between 2023-01-10 and 2022-01-01: {result2} weeks")
    result3 = calculate_week_difference('2024-05-01', '2024-04-01')
    print(f"Difference between 2024-05-01 and 2024-04-01: {result3} weeks")