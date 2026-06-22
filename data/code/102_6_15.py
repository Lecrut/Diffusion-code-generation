def is_weekday(day_index):
    try:
        if day_index in (5, 6):
            return False
        if day_index in (0, 1, 2, 3, 4):
            return True
        raise ValueError(f"Day index {day_index} is out of range 0-6")
    except TypeError:
        raise ValueError("Day index must be an integer")

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
        is_weekday(1.5)
    except ValueError as e:
        print(e)