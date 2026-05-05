class TimeCalculator:
    def elapsed_time_in_hours(self, start_time: str, end_time: str) -> float:
        from datetime import datetime
        time_format = "%H:%M"
        start = datetime.strptime(start_time, time_format)
        end = datetime.strptime(end_time, time_format)
        time_difference = end - start
        return time_difference.total_seconds() / 3600.0
if __name__ == '__main__':
    calculator = TimeCalculator()
    start = "09:00"
    end = "17:30"
    result = calculator.elapsed_time_in_hours(start, end)
    print(result)