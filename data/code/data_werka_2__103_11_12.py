class TimeDeltaCalculator:
    SECONDS_PER_MINUTE = 60
    SECONDS_PER_HOUR = 3600
    SECONDS_PER_DAY = 86400

    @staticmethod
    def get_seconds_since_start_of_day() -> float:
        import datetime
        now = datetime.datetime.now()
        seconds_today = (now.hour * TimeDeltaCalculator.SECONDS_PER_HOUR +
                         now.minute * TimeDeltaCalculator.SECONDS_PER_MINUTE +
                         now.second)
        return float(seconds_today + now.microsecond / 1000000.0)

if __name__ == '__main__':
    calculator = TimeDeltaCalculator()
    result = calculator.get_seconds_since_start_of_day()
    print(result)