class DayChecker:

    def is_weekday(self, day_index):
        return 0 <= day_index < 5
if __name__ == '__main__':
    checker = DayChecker()
    print(checker.is_weekday(1))
    print(checker.is_weekday(5))
    print(checker.is_weekday(6))