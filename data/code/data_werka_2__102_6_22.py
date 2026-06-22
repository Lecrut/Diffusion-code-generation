def is_weekday(day_index):
    DAY_MAP = {
        0: True,
        1: True,
        2: True,
        3: True,
        4: True,
        5: False,
        6: False
    }
    if day_index not in DAY_MAP:
        raise ValueError(f"Invalid day index: {day_index}")
    return DAY_MAP[day_index]

if __name__ == '__main__':
    print(is_weekday(0))
    print(is_weekday(3))
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