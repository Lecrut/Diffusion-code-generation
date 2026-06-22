from datetime import date

def check_weekend(day):
    return day.weekday() >= 5

if __name__ == '__main__':
    sample_date1 = date(2023, 10, 29)
    print(check_weekend(sample_date1))
    
    sample_date2 = date(2023, 10, 30)
    print(check_weekend(sample_date2))