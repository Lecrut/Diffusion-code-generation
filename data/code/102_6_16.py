class WeekdayValidator:
    def __init__(self):
        self._weekend_indices = frozenset([5, 6])
    
    def is_weekday(self, day_index):
        if not isinstance(day_index, int):
            raise ValueError("Day index must be an integer")
        if day_index < 0 or day_index > 6:
            raise ValueError("Day index must be between 0 and 6")
        return day_index not in self._weekend_indices

if __name__ == '__main__':
    validator = WeekdayValidator()
    print(validator.is_weekday(0))
    print(validator.is_weekday(4))
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