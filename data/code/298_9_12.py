from datetime import datetime, timedelta

class TimeDifferenceCalculator:
    def __init__(self):
        self.format_str = "%H:%M"

    def calculate_minutes(self, time1: str, time2: str) -> int:
        start_time = datetime.strptime(time1, self.format_str)
        end_time = datetime.strptime(time2, self.format_str)
        if end_time < start_time:
            end_time += timedelta(days=1)
        return (end_time - start_time).seconds // 60

if __name__ == '__main__':
    calculator = TimeDifferenceCalculator()
    print(calculator.calculate_minutes('09:45', '23:15'))