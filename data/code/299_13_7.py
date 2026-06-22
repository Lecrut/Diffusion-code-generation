from datetime import date

WEEKEND_START = 5
WEEKEND_END = 6

def is_weekend(day):
    return WEEKEND_START <= day.weekday() <= WEEKEND_END

if __name__ == '__main__':
    sample_date1 = date(2023, 10, 21)
    print(is_weekend(sample_date1))
    
    sample_date2 = date(2023, 10, 22)
    print(is_weekend(sample_date2))