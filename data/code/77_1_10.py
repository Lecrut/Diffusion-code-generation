class TimeConverter:
    MINUTES_PER_HOUR = 60

    @staticmethod
    def time_to_minutes(time_str):
        h, m, s = map(int, time_str.split(':'))
        return h * TimeConverter.MINUTES_PER_HOUR + m + s / 60.0

if __name__ == '__main__':
    converter = TimeConverter()
    print(f"Time: 01:30:00, Minutes: {converter.time_to_minutes('01:30:00')}")
    print(f"Time: 00:05:30, Minutes: {converter.time_to_minutes('00:05:30')}")
    print(f"Time: 23:59:59, Minutes: {converter.time_to_minutes('23:59:59')}")