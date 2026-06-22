class TimeConverter:
    def __init__(self, time_str):
        self.time_str = time_str

    def time_to_seconds(self):
        hours, minutes, seconds = map(int, self.time_str.split(':'))
        return hours * 3600 + minutes * 60 + seconds

    def seconds_to_human_readable(self, total_seconds):
        days = total_seconds // (24 * 3600)
        total_seconds %= (24 * 3600)
        hours = total_seconds // 3600
        total_seconds %= 3600
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        return f"{days} days, {hours} hours, {minutes} minutes"

    def convert_time(self):
        total_seconds = self.time_to_seconds()
        human_readable = self.seconds_to_human_readable(total_seconds)
        return human_readable

if __name__ == '__main__':
    sample_time1 = '24:00:00'
    converter1 = TimeConverter(sample_time1)
    result1 = converter1.convert_time()
    print(result1)

    sample_time2 = '12:34:56'
    converter2 = TimeConverter(sample_time2)
    result2 = converter2.convert_time()
    print(result2)