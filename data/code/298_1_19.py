from datetime import datetime

class TimeDeltaCalculator:
    def calculate_time_difference(self, time1_str, time2_str):
        format_str = "%H:%M"
        time1 = datetime.strptime(time1_str, format_str)
        time2 = datetime.strptime(time2_str, format_str)
        return abs((time2 - time1).total_seconds())

if __name__ == '__main__':
    calculator = TimeDeltaCalculator()
    time1 = "14:30"
    time2 = "16:45"
    difference = calculator.calculate_time_difference(time1, time2)
    print(difference)