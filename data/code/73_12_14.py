class TimeCalculator:
    SECONDS_PER_HOUR = 3600

    @staticmethod
    def diff(start_time, end_time):
        if not isinstance(start_time, (int, float)) or not isinstance(end_time, (int, float)):
            raise TypeError('Both start_time and end_time must be Unix timestamps as integers or floats')
        time_difference = abs(end_time - start_time)
        hours = time_difference / TimeCalculator.SECONDS_PER_HOUR
        return hours
if __name__ == '__main__':
    calculator = TimeCalculator()
    result = calculator.diff(1633072800, 1633076400)
    print(result)