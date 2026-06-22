class TimeCalculator:
    MINUTE_TO_SECONDS = 60

    @staticmethod
    def time_to_seconds(time_str):
        hours, minutes = map(int, time_str.split(':'))
        return hours * TimeCalculator.MINUTE_TO_SECONDS + minutes

    @staticmethod
    def absolute_time_difference(time1, time2):
        diff_seconds = abs(TimeCalculator.time_to_seconds(time1) - TimeCalculator.time_to_seconds(time2))
        return diff_seconds // TimeCalculator.MINUTE_TO_SECONDS

if __name__ == '__main__':
    time_a = '08:15'
    time_b = '20:45'
    difference = TimeCalculator.absolute_time_difference(time_a, time_b)
    print(difference)