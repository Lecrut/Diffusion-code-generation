from datetime import datetime

class TimeCalculator:
    def calculate_difference(self, time1: datetime, time2: datetime) -> str:
        difference = abs(time2 - time1)
        hours = difference.seconds // 3600
        minutes = (difference.seconds // 60) % 60
        return f"{hours}h {minutes}m"

if __name__ == '__main__':
    calculator = TimeCalculator()
    sample_time1 = datetime(2023, 11, 1, 8, 45, 0)
    sample_time2 = datetime(2023, 11, 1, 17, 30, 0)
    result = calculator.calculate_difference(sample_time1, sample_time2)
    print(f"Time 1: {sample_time1}")
    print(f"Time 2: {sample_time2}")
    print(f"Difference: {result}")