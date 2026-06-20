from datetime import datetime

class TimeCalculator:
    def calculate_difference(self, time1: datetime, time2: datetime) -> str:
        if not isinstance(time1, datetime) or not isinstance(time2, datetime):
            raise ValueError("Both inputs must be instances of datetime.")
        
        difference = abs(time2 - time1)
        hours, remainder = divmod(difference.total_seconds(), 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{int(hours)} hours, {int(minutes)} minutes, and {int(seconds)} seconds"

if __name__ == '__main__':
    calculator = TimeCalculator()
    time1 = datetime(2023, 1, 1, 10, 0, 0)
    time2 = datetime(2023, 1, 5, 14, 30, 0)
    difference = calculator.calculate_difference(time1, time2)
    print(f"Time 1: {time1}")
    print(f"Time 2: {time2}")
    print(f"Difference: {difference}")