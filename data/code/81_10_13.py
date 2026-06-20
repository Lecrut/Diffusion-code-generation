class TimeCalculator:
    def elapsed_time_in_hours(self, start_time: str, end_time: str) -> float:
        start_parts = list(map(int, start_time.split(':')))
        end_parts = list(map(int, end_time.split(':')))
        return (end_parts[0] * 3600 + end_parts[1] * 60 + end_parts[2]) / 3600 - \
               (start_parts[0] * 3600 + start_parts[1] * 60 + start_parts[2]) / 3600

if __name__ == '__main__':
    calculator = TimeCalculator()
    print(calculator.elapsed_time_in_hours('12:00', '14:30'))