from datetime import date

def years_difference(date1: date, date2: date) -> int:
    return abs((date2 - date1).days // 365)

if __name__ == '__main__':
    sample_date1 = date(1990, 5, 15)
    sample_date2 = date(2023, 8, 20)
    print(years_difference(sample_date1, sample_date2))