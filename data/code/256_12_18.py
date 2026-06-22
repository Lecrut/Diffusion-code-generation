from datetime import datetime

def date_range_difference(date1: str, date2: str) -> int:
    return abs((datetime.strptime(date2, '%Y-%m-%d') - datetime.strptime(date1, '%Y-%m-%d')).days)

if __name__ == '__main__':
    print(date_range_difference('2023-01-01', '2023-01-15'))