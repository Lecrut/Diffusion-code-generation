class TimeDifferenceCalculator:
    @staticmethod
    def time_to_minutes(time_str):
        hours, minutes = map(int, time_str.split(':'))
        return hours * 60 + minutes

    @staticmethod
    def absolute_time_difference(time1, time2):
        diff = abs(TimeDifferenceCalculator.time_to_minutes(time1) - TimeDifferenceCalculator.time_to_minutes(time2))
        if time1 > time2:
            diff = -diff
        return diff

if __name__ == '__main__':
    result = TimeDifferenceCalculator.absolute_time_difference('08:15', '20:45')
    print(result)