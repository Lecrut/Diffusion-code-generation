def is_weekday(day_index):
    WEEKDAYS = (0, 1, 2, 3, 4)
    if not isinstance(day_index, int) or day_index < 0 or day_index > 6:
        raise ValueError(f"Invalid day index: {day_index}")
    return day_index in WEEKDAYS

if __name__ == '__main__':
    print(is_weekday(0))
    print(is_weekday(1))
    print(is_weekday(4))
    print(is_weekday(5))
    print(is_weekday(6))
    try:
        is_weekday(7)
    except ValueError as e:
        print(e)
    try:
        is_weekday(-1)
    except ValueError as e:
        print(e)