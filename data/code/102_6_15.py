weekday_map = {0: False, 1: True, 2: True, 3: True, 4: True, 5: False, 6: False}

def is_weekday(day_index):
    return weekday_map.get(day_index, False)
if __name__ == '__main__':
    print(is_weekday(0))
    print(is_weekday(1))
    print(is_weekday(2))
    print(is_weekday(3))
    print(is_weekday(4))
    print(is_weekday(5))
    print(is_weekday(6))