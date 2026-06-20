from datetime import datetime

class TimeCalculator:
    def elapsed_time_in_hours(self, start_time: str, end_time: str) -> float:
        time_format = "%H:%M"
        start_dt = datetime.strptime(start_time, time_format)
        end_dt = datetime.strptime(end_time, time_format)
        delta = end_dt - start_dt
        return abs(delta.total_seconds() / 3600)

if __name__ == '__main__':
    calculator = TimeCalculator()
    result = calculator.elapsed_time_in_hours("14:30", "18:45")
    print(result)