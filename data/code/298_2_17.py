class TimeDeltaCalculator:
    SECONDS_PER_MINUTE = 60
    MINUTES_PER_HOUR = 60
    
    @staticmethod
    def time_to_seconds(time_str: str) -> int:
        hours, minutes, seconds = map(int, time_str.split(':'))
        return hours * TimeDeltaCalculator.SECONDS_PER_MINUTE * TimeDeltaCalculator.MINUTES_PER_HOUR + \
               minutes * TimeDeltaCalculator.SECONDS_PER_MINUTE + seconds
    
    @staticmethod
    def seconds_to_time(seconds: int) -> str:
        hours = seconds // (TimeDeltaCalculator.SECONDS_PER_MINUTE * TimeDeltaCalculator.MINUTES_PER_HOUR)
        minutes = (seconds % (TimeDeltaCalculator.SECONDS_PER_MINUTE * TimeDeltaCalculator.MINUTES_PER_HOUR)) // TimeDeltaCalculator.SECONDS_PER_MINUTE
        seconds = seconds % TimeDeltaCalculator.SECONDS_PER_MINUTE
        return f"{hours:02}:{minutes:02}:{seconds:02}"
    
    @staticmethod
    def time_difference(time1: str, time2: str) -> tuple:
        seconds_diff = abs(TimeDeltaCalculator.time_to_seconds(time2) - TimeDeltaCalculator.time_to_seconds(time1))
        hours = seconds_diff // (TimeDeltaCalculator.SECONDS_PER_MINUTE * TimeDeltaCalculator.MINUTES_PER_HOUR)
        minutes = (seconds_diff % (TimeDeltaCalculator.SECONDS_PER_MINUTE * TimeDeltaCalculator.MINUTES_PER_HOUR)) // TimeDeltaCalculator.SECONDS_PER_MINUTE
        seconds = seconds_diff % TimeDeltaCalculator.SECONDS_PER_MINUTE
        return hours, minutes, seconds

if __name__ == '__main__':
    print(TimeDeltaCalculator.time_difference("12:00:00", "14:30:45"))