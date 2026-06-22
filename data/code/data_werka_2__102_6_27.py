def is_weekday(day_index):
    if not isinstance(day_index, int) or not (0 <= day_index <= 6):
        raise ValueError(f"Invalid day index: {day_index}")
    return day_index < 5

if __name__ == '__main__':
    print(is_weekday(0))
    print(is_weekday(4))
    print(is_weekday(5))
    print(is_weekday(6))
    try:
        print(is_weekday(7))
    except ValueError as e:
        print(e)
    try:
        print(is_weekday(-1))
    except ValueError as e:
        print(e)
    try:
        print(is_weekday(3.5))
    except ValueError as e:
        print(e)