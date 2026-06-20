import datetime

def calculate_week_difference(date1_str, date2_str):
    date_format = '%Y-%m-%d'
    date1 = datetime.datetime.strptime(date1_str, date_format)
    date2 = datetime.datetime.strptime(date2_str, date_format)
    delta = abs((date2 - date1).days)
    weeks = delta // 7
    return weeks

if __name__ == '__main__':
    result1 = calculate_week_difference('2023-01-01', '2023-01-15')
    print(f"Difference between 2023-01-01 and 2023-01-15: {result1} weeks")
    result2 = calculate_week_difference('2023-01-15', '2022-01-01')
    print(f"Difference between 2023-01-15 and 2022-01-01: {result2} weeks")
    result3 = calculate_week_difference('2024-05-01', '2024-04-01')
    print(f"Difference between 2024-05-01 and 2024-04-01: {result3} weeks")