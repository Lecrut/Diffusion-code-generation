def is_weekday(day_index):
    if day_index < 0 or day_index > 6:
        raise ValueError("day_index must be between 0 and 6")
    weekend_indices = (5, 6)
    if day_index in weekend_indices:
        return False
    return True

if __name__ == '__main__':
    test_cases = (0, 1, 2, 3, 4, 5, 6, 7, -1)
    for idx in test_cases:
        try:
            result = is_weekday(idx)
            print(result)
        except ValueError as error:
            print(error)