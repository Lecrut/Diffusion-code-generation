class DayValidator:
    def __init__(self):
        self._weekend_set = frozenset([5, 6])
        self._valid_range = range(0, 7)

    def check_is_weekday(self, day_index):
        if day_index not in self._valid_range:
            raise ValueError("Day index must be between 0 and 6")
        return day_index not in self._weekend_set

if __name__ == '__main__':
    validator = DayValidator()
    print(validator.check_is_weekday(0))
    print(validator.check_is_weekday(3))
    print(validator.check_is_weekday(4))
    print(validator.check_is_weekday(5))
    print(validator.check_is_weekday(6))