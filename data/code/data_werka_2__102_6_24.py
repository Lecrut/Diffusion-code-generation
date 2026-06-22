class WorkdayValidator:
    def __init__(self):
        self.weekend_indices = frozenset([5, 6])

    def is_weekday(self, day_index):
        if not isinstance(day_index, int) or day_index < 0 or day_index > 6:
            raise ValueError("day_index must be an integer between 0 and 6")
        return day_index not in self.weekend_indices

if __name__ == '__main__':
    validator = WorkdayValidator()
    print(validator.is_weekday(0))
    print(validator.is_weekday(3))
    print(validator.is_weekday(5))
    print(validator.is_weekday(6))
    print(validator.is_weekday(4))