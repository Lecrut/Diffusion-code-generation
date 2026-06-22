class TimeDifferenceCalculator:
    SECONDS_PER_MINUTE = 60
    MINUTES_PER_HOUR = 60

    @staticmethod
    def time_to_seconds(time_str):
        hours, minutes, seconds = map(int, time_str.split(':'))
        return hours * TimeDifferenceCalculator.SECONDS_PER_MINUTE * TimeDifferenceCalculator.MINUTES_PER_HOUR + \
               minutes * TimeDifferenceCalculator.SECONDS_PER_MINUTE + seconds

    @staticmethod
    def difference_in_hours_and_minutes(time1_str, time2_str):
        total_seconds1 = TimeDifferenceCalculator.time_to_seconds(time1_str)
        total_seconds2 = TimeDifferenceCalculator.time_to_seconds(time2_str)
        difference_seconds = abs(total_seconds1 - total_seconds2)
        hours = difference_seconds // (TimeDifferenceCalculator.SECONDS_PER_MINUTE * TimeDifferenceCalculator.MINUTES_PER_HOUR)
        minutes = (difference_seconds % (TimeDifferenceCalculator.SECONDS_PER_MINUTE * TimeDifferenceCalculator.MINUTES_PER_HOUR)) // TimeDifferenceCalculator.SECONDS_PER_MINUTE
        return f"{hours:02d}:{minutes:02d}"

if __name__ == '__main__':
    calculator = TimeDifferenceCalculator()
    time_a = "01:00:00"
    time_b = "05:30:45"
    result = calculator.difference_in_hours_and_minutes(time_a, time_b)
    print(result)