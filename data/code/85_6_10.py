from datetime import date

def weeks_difference(date1: date, date2: date) -> int:
    delta = abs((date2 - date1).days)
    return delta // 7

if __name__ == '__main__':
    sample_date1 = date(2023, 1, 1)
    sample_date2 = date(2023, 1, 15)
    print(weeks_difference(sample_date1, sample_date2))