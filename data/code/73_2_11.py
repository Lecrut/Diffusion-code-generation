from datetime import datetime

class TimeCalculator:
    def calculate_difference(self, time1: datetime, time2: datetime) -> str:
        difference = abs(time2 - time1)
        hours = difference.seconds // 3600
        minutes = (difference.seconds % 3600) // 60
        seconds = difference.seconds % 60
        return f"{hours}h {minutes}m {seconds}s"

if __name__ == '__main__':
    calculator = TimeCalculator()
    time1 = datetime(2023, 1, 1, 10, 0, 0)
    time2 = datetime(2023, 1, 5, 14, 30, 0)
    result = calculator.calculate_difference(time1, time2)
    print(f"Time 1: {time1}")
    print(f"Time 2: {time2}")
    print(f"Difference: {result}")