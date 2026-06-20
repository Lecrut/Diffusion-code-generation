class TimeConverter:
    HOURS_TO_MINUTES = 60

    @staticmethod
    def time_to_minutes(time_str: str) -> float:
        try:
            parts = time_str.split(':')
            if len(parts) != 3:
                raise ValueError('Invalid time format')
            hours, minutes, seconds = map(int, parts)
            return hours * TimeConverter.HOURS_TO_MINUTES + minutes + seconds / TimeConverter.HOURS_TO_MINUTES
        except (ValueError, TypeError):
            raise ValueError('Invalid time format')
if __name__ == '__main__':
    print(TimeConverter.time_to_minutes('1:30:45'))