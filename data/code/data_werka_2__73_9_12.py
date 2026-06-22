from datetime import datetime

def calculate_days_between(date1_str: str, date2_str: str) -> int:
    date1 = datetime.strptime(date1_str, '%Y-%m-%d')
    date2 = datetime.strptime(date2_str, '%Y-%m-%d')
    delta = date2 - date1
    return delta.days

if __name__ == '__main__':
    result = calculate_days_between('2023-01-01', '2023-12-31')
    print(result)