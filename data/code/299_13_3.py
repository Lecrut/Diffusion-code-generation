from datetime import date

def is_weekend(day):
    return day.weekday() >= 5

if __name__ == '__main__':
    sample_date1 = date(2023, 11, 4)
    print(is_weekend(sample_date1))
    
    sample_date2 = date(2023, 11, 5)
    print(is_weekend(sample_date2))