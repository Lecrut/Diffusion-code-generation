from datetime import datetime

class TimeDurationCalculator:
    START_TIME = "11:30"
    END_TIME = "14:15"

    @staticmethod
    def calculate_duration(start_time=START_TIME, end_time=END_TIME):
        start = datetime.strptime(start_time, '%H:%M')
        end = datetime.strptime(end_time, '%H:%M')
        duration = (end - start).seconds
        return duration

if __name__ == '__main__':
    print(TimeDurationCalculator.calculate_duration())