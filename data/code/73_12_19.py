class TimeCalculator:
    SECONDS_PER_HOUR = 3600

    @staticmethod
    def to_timestamp(value):
        if isinstance(value, int) or isinstance(value, float):
            return value
        raise ValueError('value must be a Unix timestamp (int or float)')

    def diff(self, start_time, end_time):
        start_timestamp = self.to_timestamp(start_time)
        end_timestamp = self.to_timestamp(end_time)
        time_difference = end_timestamp - start_timestamp
        hours = time_difference / self.SECONDS_PER_HOUR
        return hours
if __name__ == '__main__':
    calculator = TimeCalculator()
    result = calculator.diff(1633072800.0, 1633159200.0)
    print(result)