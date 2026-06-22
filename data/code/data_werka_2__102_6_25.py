def is_weekday(day_index):
    if not isinstance(day_index, int):
        raise ValueError("day_index must be an integer")
    if day_index < 0 or day_index > 6:
        raise ValueError("day_index must be between 0 and 6")
    return day_index < 5

if __name__ == '__main__':
    print(is_weekday(0))
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
    try:
        is_weekday(2.5)
    except ValueError as e:
        print(e)