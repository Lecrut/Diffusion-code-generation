import calendar

def is_weekday(year, month, day):
    try:
        return calendar.weekday(year, month, day) < 5
    except ValueError:
        raise ValueError(f"Invalid date: {year}-{month}-{day}")

if __name__ == '__main__':
    result = is_weekday(2023, 10, 23)
    print(result)
    result2 = is_weekday(2023, 10, 21)
    print(result2)