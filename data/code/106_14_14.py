import datetime
YEAR_CONVERSION = 365.25

def calculate_year_difference(date1: datetime.datetime, date2: datetime.datetime) -> int:
    delta = abs(date1 - date2)
    years_difference = delta.days / YEAR_CONVERSION
    return int(years_difference)
if __name__ == '__main__':
    sample_date1 = datetime.datetime(2023, 4, 15)
    sample_date2 = datetime.datetime(1998, 7, 20)
    difference = calculate_year_difference(sample_date1, sample_date2)
    print(f'Date 1: {sample_date1}')
    print(f'Date 2: {sample_date2}')
    print(f'The absolute difference in years is: {difference}')