from datetime import datetime

class TimeDifferenceCalculator:
    def calculate_time_difference(self, time1: str, time2: str) -> timedelta:
        format_str = '%H:%M'
        start_time = datetime.strptime(time1, format_str)
        end_time = datetime.strptime(time2, format_str)
        
        if end_time < start_time:
            end_time += timedelta(days=1)
        
        difference = end_time - start_time
        return difference

if __name__ == '__main__':
    calculator = TimeDifferenceCalculator()
    result = calculator.calculate_time_difference('23:59', '00:01')
    print(result)