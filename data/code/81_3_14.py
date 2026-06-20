class TimeCalculator:
    TIME_FORMAT = "%H:%M:%S"
    
    @staticmethod
    def convert_to_seconds(time_str):
        hours, minutes, seconds = map(int, time_str.split(':'))
        return hours * 3600 + minutes * 60 + seconds
    
    def calculate_difference(self, start_time_str, end_time_str):
        start_seconds = self.convert_to_seconds(start_time_str)
        end_seconds = self.convert_to_seconds(end_time_str)
        difference_in_seconds = abs(end_seconds - start_seconds)
        difference_in_hours = difference_in_seconds // 3600
        return difference_in_hours

if __name__ == '__main__':
    calculator = TimeCalculator()
    elapsed = calculator.calculate_difference('09:00:00', '17:30:00')
    print(f"{elapsed}")