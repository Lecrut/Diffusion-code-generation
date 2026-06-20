class WeekdayChecker:
    def is_weekday(self, day_index):
        return 0 <= day_index < 5

if __name__ == '__main__':
    checker = WeekdayChecker()
    sample_days = [0, 1, 2, 3, 4, 5, 6]
    for day in sample_days:
        print(f"Day {day}: {'Weekday' if checker.is_weekday(day) else 'Not a weekday'}")