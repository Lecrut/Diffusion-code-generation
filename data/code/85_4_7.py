from datetime import date

def week_difference(start_date: date, end_date: date) -> int:
    if start_date > end_date:
        raise ValueError('Start date cannot be after end date')
    return (end_date - start_date).days // 7
if __name__ == '__main__':
    print(week_difference(date(2023, 1, 1), date(2023, 1, 8)))
    print(week_difference(date(2023, 1, 1), date(2023, 1, 7)))
    print(week_difference(date(2023, 1, 8), date(2023, 1, 1)))