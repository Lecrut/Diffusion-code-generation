from datetime import datetime, time, timedelta

class TimeCalculator:
    SECONDS_PER_HOUR = 3600
    SECONDS_PER_MINUTE = 60

    @staticmethod
    def get_midnight_of_date(d):
        return datetime.combine(d, time.min)

    @staticmethod
    def calculate_elapsed_since_midnight(reference_dt):
        midnight = TimeCalculator.get_midnight_of_date(reference_dt.date())
        delta = reference_dt - midnight
        total_seconds = int(delta.total_seconds())
        hours = total_seconds // TimeCalculator.SECONDS_PER_HOUR
        remainder = total_seconds % TimeCalculator.SECONDS_PER_HOUR
        minutes = remainder // TimeCalculator.SECONDS_PER_MINUTE
        seconds = remainder % TimeCalculator.SECONDS_PER_MINUTE
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

if __name__ == '__main__':
    sample_dt = datetime(2023, 11, 15, 10, 5, 30)
    result = TimeCalculator.calculate_elapsed_since_midnight(sample_dt)
    print(result)