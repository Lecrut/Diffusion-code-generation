class TimeConverter:
    MINUTES_PER_HOUR = 60
    SECONDS_TO_MINUTES = 1 / 60

    @staticmethod
    def time_to_minutes(time_str):
        h, m, s = map(int, time_str.split(':'))
        total_minutes = (h * TimeConverter.MINUTES_PER_HOUR) + m + s * TimeConverter.SECONDS_TO_MINUTES
        return total_minutes

if __name__ == '__main__':
    converter = TimeConverter()
    times = ["01:30:00", "00:05:30", "23:59:59"]
    for time in times:
        result = converter.time_to_minutes(time)
        print(f"Time: {time}, Minutes: {result}")