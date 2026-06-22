def is_weekday(day_index):
    days = {0: True, 1: True, 2: True, 3: True, 4: True, 5: False, 6: False}
    if day_index not in days:
        raise ValueError("Day index must be between 0 and 6")
    return days[day_index]

if __name__ == '__main__':
    print(is_weekday(0))
    print(is_weekday(4))
    print(is_weekday(5))
    print(is_weekday(6))