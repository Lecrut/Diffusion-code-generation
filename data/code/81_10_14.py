class TimeCalculator:
    def elapsed_time_in_hours(self, start_time: str, end_time: str) -> float:
        start_parts = list(map(int, start_time.split(':')))
        end_parts = list(map(int, end_time.split(':')))
        start_minutes = start_parts[0] * 60 + start_parts[1]
        end_minutes = end_parts[0] * 60 + end_parts[1]
        elapsed_minutes = (end_minutes - start_minutes) % (24 * 60)
        return elapsed_minutes / 60

if __name__ == '__main__':
    calculator = TimeCalculator()
    print(calculator.elapsed_time_in_hours('09:30', '17:45'))