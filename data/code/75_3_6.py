from datetime import datetime, timedelta

def date_difference(date1: str, date2: str) -> timedelta:
    return abs(datetime.strptime(date1, '%Y-%m-%d') - datetime.strptime(date2, '%Y-%m-%d'))

if __name__ == '__main__':
    print(date_difference('2023-10-01', '2023-09-15'))