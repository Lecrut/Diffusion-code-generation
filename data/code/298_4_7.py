class TimeCalculator:
    MINUTES_PER_HOUR = 60

    @staticmethod
    def time_to_minutes(time_str):
        hour, minute = map(int, time_str.split(':'))
        return hour * TimeCalculator.MINUTES_PER_HOUR + minute

    @staticmethod
    def minutes_difference(start_time, end_time):
        start_minutes = TimeCalculator.time_to_minutes(start_time)
        end_minutes = TimeCalculator.time_to_minutes(end_time)
        if start_minutes > end_minutes:
            end_minutes += 24 * TimeCalculator.MINUTES_PER_HOUR
        return (end_minutes - start_minutes) // TimeCalculator.MINUTES_PER_HOUR

if __name__ == '__main__':
    time_a = "07:45"
    time_b = "18:23"
    result = TimeCalculator.minutes_difference(time_a, time_b)
    print(f"Duration between {time_a} and {time_b}: {result} minutes")