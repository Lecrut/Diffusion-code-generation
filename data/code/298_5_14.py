class TimeCalculator:
    def __init__(self):
        self.time_format = "%H:%M"

    def time_to_seconds(self, time_str):
        return datetime.datetime.strptime(time_str, self.time_format).time()

    def seconds_to_hours(self, seconds):
        return seconds / 3600

    def time_difference_in_hours(self, time1_str, time2_str):
        time1 = self.time_to_seconds(time1_str)
        time2 = self.time_to_seconds(time2_str)
        if time2 > time1:
            diff = (time2 - datetime.datetime.min.time()).total_seconds()
            return self.seconds_to_hours(diff)
        else:
            raise ValueError("Second time is not chronologically after the first time")

if __name__ == '__main__':
    calculator = TimeCalculator()
    try:
        result = calculator.time_difference_in_hours("19:30", "12:00")
        print(result)
    except ValueError as e:
        print(f"Error: {e}")