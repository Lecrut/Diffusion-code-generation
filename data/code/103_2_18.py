import time
from datetime import datetime, timedelta

SECONDS_PER_HOUR = 3600
SECONDS_PER_MINUTE = 60
SECONDS_PER_DAY = 86400

class ElapsedTimeCalculator:
    def __init__(self):
        self.now_timestamp = None

    def _get_current_time(self):
        return time.time()

    def _calculate_midnight_offset(self, current_time):
        epoch = datetime(1970, 1, 1)
        dt = epoch + timedelta(seconds=current_time)
        midnight_dt = dt.replace(hour=0, minute=0, second=0, microsecond=0)
        midnight_timestamp = (midnight_dt - epoch).total_seconds()
        return current_time - midnight_timestamp

    def get_elapsed_hours_minutes_seconds(self):
        self.now_timestamp = self._get_current_time()
        elapsed_seconds = self._calculate_midnight_offset(self.now_timestamp)
        
        hours = int(elapsed_seconds // SECONDS_PER_HOUR)
        remainder_after_hours = elapsed_seconds % SECONDS_PER_HOUR
        
        minutes = int(remainder_after_hours // SECONDS_PER_MINUTE)
        seconds = remainder_after_hours % SECONDS_PER_MINUTE
        
        return (hours, minutes, seconds)

if __name__ == '__main__':
    calculator = ElapsedTimeCalculator()
    output = calculator.get_elapsed_hours_minutes_seconds()
    print(output)