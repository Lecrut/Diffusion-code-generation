from datetime import time

class TimeDifferenceCalculator:
    MIDNIGHT = time(0, 0)
    
    @staticmethod
    def calculate_difference(start_time: time, end_time: time) -> int:
        if start_time < end_time:
            return (end_time - start_time).seconds
        else:
            return (time(23, 59, 59) - start_time).seconds + (end_time - time(0, 0)).seconds + 1

if __name__ == '__main__':
    calculator = TimeDifferenceCalculator()
    difference = calculator.calculate_difference(TimeDifferenceCalculator.MIDNIGHT, time(0, 1))
    print(difference)