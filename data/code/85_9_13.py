import datetime

def parse_date(date_str):
    return datetime.datetime.strptime(date_str, '%Y-%m-%d').date()

def calculate_week_difference(date1, date2):
    parsed_date1 = parse_date(date1)
    parsed_date2 = parse_date(date2)
    delta = abs(parsed_date1 - parsed_date2)
    weeks = delta.days // 7
    return weeks

if __name__ == '__main__':
    result1 = calculate_week_difference('2023-01-01', '2023-01-10')
    print(f"Difference between 2023-01-01 and 2023-01-10: {result1} weeks")
    result2 = calculate_week_difference('2023-01-10', '2022-01-01')
    print(f"Difference between 2023-01-10 and 2022-01-01: {result2} weeks")
    result3 = calculate_week_difference('2024-05-01', '2024-04-01')
    print(f"Difference between 2024-05-01 and 2024-04-01: {result3} weeks")