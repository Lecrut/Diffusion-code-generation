from datetime import datetime, timedelta

class DayDurationCalculator:
    def __init__(self, target_datetime: datetime):
        if not isinstance(target_datetime, datetime):
            raise ValueError("target_datetime must be a datetime instance")
        self.target_datetime = target_datetime

    def get_elapsed_seconds(self) -> int:
        start_of_day = self.target_datetime.replace(hour=0, minute=0, second=0, microsecond=0)
        delta = self.target_datetime - start_of_day
        total_seconds = int(delta.total_seconds())
        return total_seconds

    def get_formatted_elapsed(self) -> str:
        total_seconds = self.get_elapsed_seconds()
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        return f"{hours}h {minutes}m {seconds}s"

def calculate_elapsed_time_since_start_of_day(target_date: datetime) -> dict:
    if not isinstance(target_date, datetime):
        raise ValueError("target_date must be a datetime object")
    
    calculator = DayDurationCalculator(target_date)
    
    elapsed_seconds = calculator.get_elapsed_seconds()
    formatted = calculator.get_formatted_elapsed()
    
    start_of_day = target_date.replace(hour=0, minute=0, second=0, microsecond=0)
    
    return {
        "target_date": target_date,
        "start_of_day": start_of_day,
        "elapsed_seconds": elapsed_seconds,
        "elapsed_formatted": formatted
    }

if __name__ == '__main__':
    sample_date = datetime(2023, 10, 5, 14, 30, 45)
    result = calculate_elapsed_time_since_start_of_day(sample_date)
    print(result)