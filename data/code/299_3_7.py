from datetime import date

def is_weekend_optimized(year, month, day):
    return date(year, month, day).weekday() >= 5
if __name__ == '__main__':
    print(is_weekend_optimized(2023, 10, 7))
    print(is_weekend_optimized(2023, 10, 8))