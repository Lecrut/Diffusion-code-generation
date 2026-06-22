import datetime
MONTH_NAMES = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}

def iso_to_readable(date_str: str) -> str:
    year, month, day = map(int, date_str.split('-'))
    return f'{day} {MONTH_NAMES[month]} {year}'
if __name__ == '__main__':
    sample_date = '2021-07-04'
    readable_date = iso_to_readable(sample_date)
    print(readable_date)