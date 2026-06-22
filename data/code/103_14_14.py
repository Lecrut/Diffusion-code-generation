import datetime

class ElapsedTimeCalculator:
    HOURS_IN_DAY = 24
    SECONDS_IN_HOUR = 3600
    SECONDS_IN_MINUTE = 60
    MINUTES_IN_HOUR = 60
    FORMAT_PATTERN = "%H:%M:%S"

    @staticmethod
    def _get_current_time():
        return datetime.datetime.now()

    @staticmethod
    def _get_start_of_day(reference_time):
        return reference_time.replace(hour=0, minute=0, second=0, microsecond=0)

    @staticmethod
    def _calculate_total_seconds(start, end):
        delta = end - start
        return int(delta.total_seconds())

    @staticmethod
    def _convert_seconds_to_hms(total_seconds):
        hours = total_seconds // ElapsedTimeCalculator.SECONDS_IN_HOUR
        remainder = total_seconds % ElapsedTimeCalculator.SECONDS_IN_HOUR
        minutes = remainder // ElapsedTimeCalculator.SECONDS_IN_MINUTE
        seconds = remainder % ElapsedTimeCalculator.SECONDS_IN_MINUTE
        return hours, minutes, seconds

    @staticmethod
    def format_elapsed_time():
        current_time = ElapsedTimeCalculator._get_current_time()
        start_time = ElapsedTimeCalculator._get_start_of_day(current_time)
        total_seconds = ElapsedTimeCalculator._calculate_total_seconds(start_time, current_time)
        hours, minutes, seconds = ElapsedTimeCalculator._convert_seconds_to_hms(total_seconds)
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

if __name__ == '__main__':
    print(ElapsedTimeCalculator.format_elapsed_time())