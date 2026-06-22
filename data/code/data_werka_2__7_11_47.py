class TimeConverter:
    SECONDS_IN_HOUR = 3600
    SECONDS_IN_MINUTE = 60
    SECONDS_IN_DAY = 86400

    @staticmethod
    def time_to_seconds(time_str):
        try:
            hours, minutes, seconds = map(int, time_str.split(':'))
            if not (0 <= hours < 24 and 0 <= minutes < 60 and 0 <= seconds < 60):
                raise ValueError("Invalid time format. Hours must be between 0-23, minutes and seconds between 0-59.")
            return hours * TimeConverter.SECONDS_IN_HOUR + minutes * TimeConverter.SECONDS_IN_MINUTE + seconds
        except ValueError as e:
            raise ValueError(f'Invalid input: {e}')

    @staticmethod
    def seconds_to_human_readable(total_seconds):
        try:
            if total_seconds < 0:
                raise ValueError('Total seconds cannot be negative.')
            days = total_seconds // TimeConverter.SECONDS_IN_DAY
            remaining_seconds = total_seconds % TimeConverter.SECONDS_IN_DAY
            hours = remaining_seconds // TimeConverter.SECONDS_IN_HOUR
            remaining_seconds %= TimeConverter.SECONDS_IN_HOUR
            minutes = remaining_seconds // TimeConverter.SECONDS_IN_MINUTE
            seconds = remaining_seconds % TimeConverter.SECONDS_IN_MINUTE
            return f"{days} days, {hours} hours, {minutes} minutes"
        except ValueError as e:
            raise ValueError(f'Invalid input: {e}')

    @staticmethod
    def convert_time(time_str):
        total_seconds = TimeConverter.time_to_seconds(time_str)
        human_readable = TimeConverter.seconds_to_human_readable(total_seconds)
        return human_readable

if __name__ == '__main__':
    sample_time = '12:34:56'
    result = TimeConverter.convert_time(sample_time)
    print(result)