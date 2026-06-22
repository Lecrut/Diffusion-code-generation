class TimeCalculator:
    TIME_FORMAT = "%H:%M"

    @staticmethod
    def time_to_seconds(time_str):
        return datetime.strptime(time_str, TimeCalculator.TIME_FORMAT).second + \
               datetime.strptime(time_str, TimeCalculator.TIME_FORMAT).minute * 60 + \
               datetime.strptime(time_str, TimeCalculator.TIME_FORMAT).hour * 3600

if __name__ == '__main__':
    start_time = '11:30'
    end_time = '14:15'
    calculator = TimeCalculator()
    duration_seconds = calculator.time_to_seconds(end_time) - calculator.time_to_seconds(start_time)
    print(duration_seconds)