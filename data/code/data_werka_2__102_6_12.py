class DayChecker:
    def __init__(self):
        self.weekend_days = {5, 6}

    def is_weekday(self, day_index):
        if not isinstance(day_index, int) or day_index < 0 or day_index > 6:
            raise ValueError("Invalid day index")
        return day_index not in self.weekend_days

if __name__ == '__main__':
    checker = DayChecker()
    print(checker.is_weekday(0))
    print(checker.is_weekday(4))
    print(checker.is_weekday(5))
    print(checker.is_weekday(6))
    try:
        checker.is_weekday(7)
    except ValueError as e:
        print(e)
    try:
        checker.is_weekday(-1)
    except ValueError as e:
        print(e)