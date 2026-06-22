from datetime import date

def is_weekend(year, month, day):
    target_date = date(year, month, day)
    return target_date.weekday() >= 5

if __name__ == '__main__':
    sample_year = 2023
    sample_month = 10
    sample_day = 7
    
    another_sample_year = 2023
    another_sample_month = 10
    another_sample_day = 9
    
    print(is_weekend(sample_year, sample_month, sample_day))
    print(is_weekend(another_sample_year, another_sample_month, another_sample_day))