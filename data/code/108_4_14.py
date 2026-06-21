import calendar

def get_day_name(year, month, day):
    _, day_of_week = calendar.monthrange(year, month)
    if not isinstance(year, int) or not isinstance(month, int) or not isinstance(day, int):
        raise ValueError("Inputs must be integers")
    if not (1 <= month <= 12):
        raise ValueError("Invalid month")
    if not (1 <= day <= 31):
        raise ValueError("Invalid day")
    max_days = calendar.monthrange(year, month)[1]
    if day > max_days:
        raise ValueError("Day out of range")
    return calendar.day_name[day_of_week]

if __name__ == '__main__':
    print(get_day_name(2023, 10, 15))