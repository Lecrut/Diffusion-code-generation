from datetime import date

def get_day_of_month(year, month, day):
    return date(year, month, day).day

if __name__ == '__main__':
    sample_date = date(2023, 10, 5)
    print(get_day_of_month(sample_date.year, sample_date.month, sample_date.day))