class TimeConverter:
    SECONDS_IN_MINUTE = 60

    @staticmethod
    def parse_time(time_str):
        if ':' in time_str:
            return list(map(int, time_str.split(':')))
        raise ValueError('Invalid time format')

    @staticmethod
    def time_to_minutes(time_str):
        try:
            hours, minutes, seconds = TimeConverter.parse_time(time_str)
            total_seconds = hours * 3600 + minutes * TimeConverter.SECONDS_IN_MINUTE + seconds
            return total_seconds / TimeConverter.SECONDS_IN_MINUTE
        except ValueError as e:
            print(f'Error: {e}')
            return None
if __name__ == '__main__':
    sample_time = '2:30:45'
    result = TimeConverter.time_to_minutes(sample_time)
    print(result)