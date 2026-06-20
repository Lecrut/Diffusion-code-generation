class TimeCalculator:
    def elapsed_time_in_hours(self, start_time: str, end_time: str) -> float:
        time_format = "%H:%M"
        start_seconds = sum(int(x) * 60 ** i for i, x in enumerate(reversed(start_time.split(':'))))
        end_seconds = sum(int(x) * 60 ** i for i, x in enumerate(reversed(end_time.split(':'))))
        elapsed_seconds = abs(end_seconds - start_seconds)
        return elapsed_seconds / 3600.0

if __name__ == '__main__':
    calculator = TimeCalculator()
    start_time_str = "14:30"
    end_time_str = "20:45"
    print(f"Elapsed Time in Hours: {calculator.elapsed_time_in_hours(start_time_str, end_time_str)}")