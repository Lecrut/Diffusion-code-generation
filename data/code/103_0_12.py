import datetime

class MidnightElapsedCalculator:
    SECONDS_PER_MINUTE = 60
    MINUTES_PER_HOUR = 60
    HOURS_PER_DAY = 24
    SECONDS_PER_HOUR = SECONDS_PER_MINUTE * MINUTES_PER_HOUR

    @staticmethod
    def get_seconds_since_midnight(reference_time: datetime.datetime = None) -> float:
        if reference_time is None:
            reference_time = datetime.datetime.now()
        midnight = reference_time.replace(hour=0, minute=0, second=0, microsecond=0)
        delta_seconds = (reference_time - midnight).total_seconds()
        return delta_seconds

    @staticmethod
    def format_elapsed(seconds: float) -> str:
        hours = int(seconds // MidnightElapsedCalculator.SECONDS_PER_HOUR)
        remainder = seconds % MidnightElapsedCalculator.SECONDS_PER_HOUR
        minutes = int(remainder // MidnightElapsedCalculator.SECONDS_PER_MINUTE)
        secs = remainder % MidnightElapsedCalculator.SECONDS_PER_MINUTE
        return f"{hours}h {minutes}m {secs:.6f}s"

if __name__ == '__main__':
    now = datetime.datetime.now()
    calculator = MidnightElapsedCalculator()
    seconds_elapsed = calculator.get_seconds_since_midnight(now)
    formatted = calculator.format_elapsed(seconds_elapsed)
    print(seconds_elapsed)
    print(formatted)