def is_weekday(day_index):
    DAY_MAP = {
        0: 'Monday',
        1: 'Tuesday',
        2: 'Wednesday',
        3: 'Thursday',
        4: 'Friday',
        5: 'Saturday',
        6: 'Sunday'
    }
    if day_index not in DAY_MAP:
        raise ValueError("Day index must be between 0 and 6")
    return DAY_MAP[day_index] not in ('Saturday', 'Sunday')

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