from datetime import datetime

class TimeDifferenceCalculator:
    SECONDS_PER_HOUR = 3600.0
    
    @staticmethod
    def time_difference_in_hours(dt1, dt2):
        difference = abs(dt2 - dt1)
        hours = difference.total_seconds() / TimeDifferenceCalculator.SECONDS_PER_HOUR
        return hours

if __name__ == '__main__':
    dt1 = datetime(2023, 3, 1, 0, 0, 0)
    dt2 = datetime(2023, 3, 2, 0, 0, 0)
    result = TimeDifferenceCalculator.time_difference_in_hours(dt1, dt2)
    print(result)