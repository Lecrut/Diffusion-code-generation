from datetime import date

def years_between_dates(start_date, end_date):
    return (end_date.year - start_date.year) - ((end_date.month, end_date.day) < (start_date.month, start_date.day))

if __name__ == '__main__':
    sample_start = date(2010, 5, 15)
    sample_end = date(2023, 8, 20)
    print(years_between_dates(sample_start, sample_end))