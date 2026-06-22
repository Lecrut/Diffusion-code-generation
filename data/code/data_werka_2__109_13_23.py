from datetime import datetime

class TimeLeftCalculator:
    def __init__(self, start_date: datetime, end_date: datetime):
        self.start_date = start_date
        self.end_date = end_date

    def calculate(self) -> dict:
        if self.start_date > self.end_date:
            raise ValueError("Start date must be before or equal to end date")
        
        delta = self.end_date - self.start_date
        total_seconds = int(delta.total_seconds())
        
        days = total_seconds // 86400
        hours = (total_seconds % 86400) // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        
        return {
            "days": days,
            "hours": hours,
            "minutes": minutes,
            "seconds": seconds,
            "total_seconds": total_seconds
        }

if __name__ == '__main__':
    start = datetime(2023, 10, 1, 0, 0, 0)
    end = datetime(2023, 10, 31, 23, 59, 59)
    
    calculator = TimeLeftCalculator(start, end)
    result = calculator.calculate()
    print(result)