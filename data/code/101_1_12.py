import calendar

class WeekdayCalculator:
    NAMES = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]

    @staticmethod
    def get_name(year, month, day):
        index = calendar.weekday(year, month, day)
        return WeekdayCalculator.NAMES[index]

if __name__ == '__main__':
    result = WeekdayCalculator.get_name(2023, 10, 5)
    print(result)