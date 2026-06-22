from datetime import datetime

def is_weekend_optimized(date):
    return date.weekday() >= 5
if __name__ == '__main__':
    sample_date = datetime(2023, 10, 7)
    print(is_weekend_optimized(sample_date))