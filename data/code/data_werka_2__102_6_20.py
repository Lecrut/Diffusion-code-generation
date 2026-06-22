class DayIndexValidator:
    def __init__(self):
        self.weekend_set = frozenset([5, 6])
        self.valid_range = range(7)

    def is_weekday(self, day_index):
        if not isinstance(day_index, int):
            raise ValueError("Index must be an integer")
        if day_index not in self.valid_range:
            raise ValueError("Index must be between 0 and 6")
        return day_index not in self.weekend_set

if __name__ == '__main__':
    validator = DayIndexValidator()
    print(validator.is_weekday(0))
    print(validator.is_weekday(3))
    print(validator.is_weekday(5))
    print(validator.is_weekday(6))
    try:
        validator.is_weekday(7)
    except ValueError as e:
        print(e)
    try:
        validator.is_weekday(-1)
    except ValueError as e:
        print(e)