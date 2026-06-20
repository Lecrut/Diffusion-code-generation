import calendar

def get_day_number(year: int, month: int, day: int) -> int:
    if year < 1:
        raise ValueError("Year must be positive")
    if not (1 <= month <= 12):
        raise ValueError("Month must be between 1 and 12")
    _, days_in_month = calendar.monthrange(year, month)
    if day < 1 or day > days_in_month:
        raise ValueError(f"Day must be between 1 and {days_in_month}")
    
    return sum(calendar.monthrange(year, m)[1] for m in range(1, month)) + day

if __name__ == '__main__':
    print(get_day_number(2023, 1, 1))
    print(get_day_number(2024, 2, 29))
    print(get_day_number(2024, 3, 1))