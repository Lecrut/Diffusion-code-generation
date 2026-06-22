from datetime import datetime

class TimeDifferenceCalculator:
    def calculate_difference(self, time1: str, time2: str) -> int:
        format_str = '%H:%M'
        tdelta = datetime.strptime(time2, format_str) - datetime.strptime(time1, format_str)
        return abs(tdelta.seconds // 60)

if __name__ == '__main__':
    calculator = TimeDifferenceCalculator()
    result = calculator.calculate_difference('23:59', '00:01')
    print(result)