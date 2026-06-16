from datetime import datetime
class TimeCalculator:
    def get_difference(self, time1_str, time2_str):
        time1 = datetime.strptime(time1_str, '%H:%M')
        time2 = datetime.strptime(time2_str, '%H:%M')
        return abs(time1 - time2)
if __name__ == '__main__':
    calculator = TimeCalculator()
    time1 = "09:30"
    time2 = "14:45"
    difference = calculator.get_difference(time1, time2)
    print(difference)