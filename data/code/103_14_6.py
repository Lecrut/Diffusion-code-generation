import datetime

class ElapsedTimeFormatter:
    SECONDS_PER_HOUR = 3600
    SECONDS_PER_MINUTE = 60

    @staticmethod
    def calculate_elapsed_seconds():
        current_time = datetime.datetime.now()
        start_of_day = current_time.replace(hour=0, minute=0, second=0, microsecond=0)
        delta = current_time - start_of_day
        return int(delta.total_seconds())

    @staticmethod
    def format_elapsed(total_seconds):
        hours = total_seconds // ElapsedTimeFormatter.SECONDS_PER_HOUR
        remaining = total_seconds % ElapsedTimeFormatter.SECONDS_PER_HOUR
        minutes = remaining // ElapsedTimeFormatter.SECONDS_PER_MINUTE
        seconds = remaining % ElapsedTimeFormatter.SECONDS_PER_MINUTE
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

if __name__ == '__main__':
    total_seconds = ElapsedTimeFormatter.calculate_elapsed_seconds()
    formatted_time = ElapsedTimeFormatter.format_elapsed(total_seconds)
    print(formatted_time)