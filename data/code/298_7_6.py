import datetime

class TimeCalculator:
    @staticmethod
    def time_to_seconds(time_str):
        hours, minutes = map(int, time_str.split(':'))
        return hours * 3600 + minutes * 60

    @staticmethod
    def calculate_duration(start_time, end_time):
        start_seconds = TimeCalculator.time_to_seconds(start_time)
        end_seconds = TimeCalculator.time_to_seconds(end_time)
        return end_seconds - start_seconds

if __name__ == '__main__':
    duration = TimeCalculator.calculate_duration('11:30', '14:15')
    print(f"Total time duration: {duration} seconds")