class TimeConverter:
    def __init__(self, time_str):
        self.time_str = time_str

    def _time_to_seconds(self):
        hours, minutes, seconds = map(int, self.time_str.split(':'))
        return hours * 3600 + minutes * 60 + seconds

    def _seconds_to_human_readable(self, total_seconds):
        days = total_seconds // (24 * 3600)
        total_seconds %= (24 * 3600)
        hours = total_seconds // 3600
        total_seconds %= 3600
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        return f"{days} days, {hours} hours, {minutes} minutes"

    def convert(self):
        total_seconds = self._time_to_seconds()
        human_readable = self._seconds_to_human_readable(total_seconds)
        return human_readable

if __name__ == '__main__':
    sample_time1 = '12:34:56'
    sample_time2 = '48:30:15'

    converter1 = TimeConverter(sample_time1)
    result1 = converter1.convert()

    converter2 = TimeConverter(sample_time2)
    result2 = converter2.convert()

    print(result1)
    print(result2)