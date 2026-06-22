from datetime import time, timedelta

class ElapsedTimeCalculator:
    def __init__(self, current_time: time):
        self.current_time = current_time

    def calculate(self):
        midnight = time(0, 0, 0)
        if self.current_time < midnight:
            raise ValueError("Time cannot be before midnight")
        
        delta = timedelta(
            hours=self.current_time.hour,
            minutes=self.current_time.minute,
            seconds=self.current_time.second
        )
        
        total_seconds = int(delta.total_seconds())
        hours = total_seconds // 3600
        remaining_seconds = total_seconds % 3600
        minutes = remaining_seconds // 60
        seconds = remaining_seconds % 60
        
        return {
            "hours": hours,
            "minutes": minutes,
            "seconds": seconds
        }

if __name__ == '__main__':
    sample_time = time(14, 30, 45)
    calculator = ElapsedTimeCalculator(sample_time)
    result = calculator.calculate()
    print(result)