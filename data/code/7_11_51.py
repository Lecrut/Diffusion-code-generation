class TimeConverter:
    SECONDS_IN_HOUR = 3600
    SECONDS_IN_DAY = 24 * SECONDS_IN_HOUR

    @staticmethod
    def time_to_seconds(time_str):
        hours, minutes, seconds = map(int, time_str.split(':'))
        return hours * TimeConverter.SECONDS_IN_HOUR + minutes * 60 + seconds

    @staticmethod
    def seconds_to_human_readable(total_seconds):
        days = total_seconds // TimeConverter.SECONDS_IN_DAY
        remaining_seconds = total_seconds % TimeConverter.SECONDS_IN_DAY
        hours = remaining_seconds // TimeConverter.SECONDS_IN_HOUR
        remaining_seconds %= TimeConverter.SECONDS_IN_HOUR
        minutes = remaining_seconds // 60
        seconds = remaining_seconds % 60
        return f"{days} days, {hours} hours, {minutes} minutes"

    @staticmethod
    def convert_time(time_str):
        total_seconds = TimeConverter.time_to_seconds(time_str)
        human_readable = TimeConverter.seconds_to_human_readable(total_seconds)
        return human_readable

if __name__ == '__main__':
    sample_time = '23:59:59'
    result = TimeConverter.convert_time(sample_time)
    print(result)