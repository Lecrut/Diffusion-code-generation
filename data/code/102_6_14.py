def is_weekday(day_index):
    if not isinstance(day_index, int) or day_index < 0 or day_index > 6:
        raise ValueError('Day index must be an integer between 0 and 6.')
    return day_index < 5
if __name__ == '__main__':
    print(is_weekday(0))
    print(is_weekday(1))
    print(is_weekday(4))
    print(is_weekday(5))
    print(is_weekday(6))