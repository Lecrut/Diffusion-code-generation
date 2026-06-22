from datetime import datetime

class TimeCalculator:
    def parse_time(self, time_str):
        return datetime.strptime(time_str, '%H:%M')

    def get_difference_seconds(self, time1, time2):
        time1_dt = self.parse_time(time1)
        time2_dt = self.parse_time(time2)
        delta = time2_dt - time1_dt
        return abs(delta.total_seconds())

if __name__ == '__main__':
    calculator = TimeCalculator()
    time1 = "14:30"
    time2 = "16:45"
    difference_seconds = calculator.get_difference_seconds(time1, time2)
    print(difference_seconds)