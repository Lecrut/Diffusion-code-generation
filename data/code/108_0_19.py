from datetime import date

def get_day_of_month(year, month, day):
    specific_date = date(year, month, day)
    return specific_date.day

if __name__ == '__main__':
    sample_year = 2023
    sample_month = 10
    sample_day = 5
    print(get_day_of_month(sample_year, sample_month, sample_day))