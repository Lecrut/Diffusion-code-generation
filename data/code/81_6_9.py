from datetime import datetime

class TimeCalculator:
    TIME_FORMAT = '%H:%M'

    @staticmethod
    def calculate_elapsed_time(file_path):
        with open(file_path, 'r') as file:
            times = [line.strip() for line in file.readlines()]
            start_time = datetime.strptime(times[0], TimeCalculator.TIME_FORMAT)
            end_time = datetime.strptime(times[1], TimeCalculator.TIME_FORMAT)
            time_difference = end_time - start_time
            return str(time_difference)

if __name__ == '__main__':
    result = TimeCalculator.calculate_elapsed_time('times.txt')
    print(result)