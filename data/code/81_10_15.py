class TimeCalculator:
    @staticmethod
    def elapsed_time_in_hours(start_time: str, end_time: str) -> float:
        start_parts = list(map(int, start_time.split(':')))
        end_parts = list(map(int, end_time.split(':')))
        
        start_minutes = start_parts[0] * 60 + start_parts[1]
        end_minutes = end_parts[0] * 60 + end_parts[1]
        
        elapsed_minutes = end_minutes - start_minutes
        elapsed_hours = elapsed_minutes / 60.0
        
        return elapsed_hours

if __name__ == '__main__':
    calculator = TimeCalculator()
    result = calculator.elapsed_time_in_hours("10:00", "14:30")
    print(f"Elapsed Time in Hours: {result}")