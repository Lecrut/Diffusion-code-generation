from datetime import datetime

class TimeDifferenceCalculator:
    TIME_FORMAT = "%H:%M"
    
    @staticmethod
    def calculate_difference(time1_str, time2_str):
        time1 = datetime.strptime(time1_str, TimeDifferenceCalculator.TIME_FORMAT)
        time2 = datetime.strptime(time2_str, TimeDifferenceCalculator.TIME_FORMAT)
        return abs((time2 - time1).total_seconds())

if __name__ == '__main__':
    difference = TimeDifferenceCalculator.calculate_difference('14:30', '16:45')
    print(int(difference))