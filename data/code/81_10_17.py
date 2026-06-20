class TimeCalculator:
    def elapsed_time_in_hours(self, start_time: str, end_time: str) -> float:
        start_parts = map(int, start_time.split(':'))
        end_parts = map(int, end_time.split(':'))
        start_minutes = start_parts[0] * 60 + start_parts[1]
        end_minutes = end_parts[0] * 60 + end_parts[1]
        elapsed_minutes = end_minutes - start_minutes
        return elapsed_minutes / 60.0

if __name__ == '__main__':
    calculator = TimeCalculator()
    start_time = "12:30"
    end_time = "15:45"
    print(f"Elapsed time in hours: {calculator.elapsed_time_in_hours(start_time, end_time)}")