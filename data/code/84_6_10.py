import calendar

def get_day_number(year: int, month: int, day: int) -> int:
    if year < 1:
        raise ValueError("Year must be positive")
    if not (1 <= month <= 12):
        raise ValueError("Month must be between 1 and 12")
    
    return calendar.monthrange(year, month)[1] + sum(calendar.monthrange(year, m)[1] for m in range(1, month)) - calendar.monthrange(year, month)[0] + day

if __name__ == '__main__':
    print(get_day_number(2023, 1, 1))
    print(get_day_number(2024, 2, 29))
    print(get_day_number(2024, 3, 1))