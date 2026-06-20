from datetime import date

def get_day_of_month(year, month, day):
    try:
        return date(year, month, day).day
    except ValueError as e:
        raise ValueError(f'Invalid date: {e}')
if __name__ == '__main__':
    sample_dates = [(2023, 10, 5), (2024, 2, 29), (2023, 13, 1), (2023, 2, 30)]
    for year, month, day in sample_dates:
        try:
            print(f'Day of {year}-{month}-{day}: {get_day_of_month(year, month, day)}')
        except ValueError as e:
            print(e)