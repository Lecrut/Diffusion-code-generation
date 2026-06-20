def is_weekday(day_index):
    weekdays = {0: True, 1: True, 2: True, 3: True, 4: True}
    return weekdays.get(day_index, False)
if __name__ == '__main__':
    print(is_weekday(0))
    print(is_weekday(5))