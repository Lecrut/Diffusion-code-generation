class TimeDifferenceCalculator:
    SECONDS_IN_MINUTE = 60
    SECONDS_IN_HOUR = 3600

    @staticmethod
    def time_to_seconds(time_tuple):
        hours, minutes, seconds = time_tuple
        return hours * TimeDifferenceCalculator.SECONDS_IN_HOUR + \
               minutes * TimeDifferenceCalculator.SECONDS_IN_MINUTE + \
               seconds

    @staticmethod
    def seconds_to_time(seconds):
        hours = seconds // TimeDifferenceCalculator.SECONDS_IN_HOUR
        minutes = (seconds % TimeDifferenceCalculator.SECONDS_IN_HOUR) // TimeDifferenceCalculator.SECONDS_IN_MINUTE
        seconds = seconds % TimeDifferenceCalculator.SECONDS_IN_MINUTE
        return hours, minutes, seconds

    @staticmethod
    def calculate_difference(time1, time2):
        time1_seconds = TimeDifferenceCalculator.time_to_seconds(time1)
        time2_seconds = TimeDifferenceCalculator.time_to_seconds(time2)
        difference_seconds = abs(time1_seconds - time2_seconds)
        return TimeDifferenceCalculator.seconds_to_time(difference_seconds)

if __name__ == '__main__':
    sample_time1 = (3, 45, 10)
    sample_time2 = (2, 15, 50)
    result = TimeDifferenceCalculator.calculate_difference(sample_time1, sample_time2)
    print(result)