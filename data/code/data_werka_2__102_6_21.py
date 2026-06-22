def is_weekday(day_index):
    def _validate_index(idx):
        if not isinstance(idx, int):
            raise ValueError("Day index must be an integer")
        if idx < 0 or idx > 6:
            raise ValueError("Day index must be between 0 and 6")
        return idx

    def _check_weekday_status(index):
        weekend_set = frozenset([5, 6])
        return index not in weekend_set

    validated_index = _validate_index(day_index)
    return _check_weekday_status(validated_index)

if __name__ == '__main__':
    test_indices = [0, 1, 2, 3, 4, 5, 6, -1, 7]
    for idx in test_indices:
        try:
            result = is_weekday(idx)
            print(result)
        except ValueError as e:
            print(str(e))