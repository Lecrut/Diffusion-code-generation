class TimeCalculator:
    MINUTES_PER_HOUR = 60

    @staticmethod
    def parse_time(time_str):
        hours, minutes = map(int, time_str.split(':'))
        return hours * TimeCalculator.MINUTES_PER_HOUR + minutes

    @staticmethod
    def absolute_time_difference(time1, time2):
        parsed_time1 = TimeCalculator.parse_time(time1)
        parsed_time2 = TimeCalculator.parse_time(time2)
        difference = abs(parsed_time1 - parsed_time2)
        return difference if parsed_time1 <= parsed_time2 else -difference

if __name__ == '__main__':
    time_a = '08:15'
    time_b = '20:45'
    difference = TimeCalculator.absolute_time_difference(time_a, time_b)
    print(difference)