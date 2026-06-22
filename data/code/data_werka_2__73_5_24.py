from datetime import datetime, timedelta

class TimeDiffer:
    def __init__(self, reference_point: datetime):
        self.reference_point = reference_point

    def compute_delta(self, target: datetime) -> timedelta:
        return target - self.reference_point

    def get_seconds(self, target: datetime) -> float:
        delta = self.compute_delta(target)
        return delta.total_seconds()

    def format_duration(self, target: datetime) -> str:
        delta = self.compute_delta(target)
        total_seconds = int(abs(delta.total_seconds()))
        sign = "-" if delta.total_seconds() < 0 else ""
        days = total_seconds // 86400
        hours = (total_seconds % 86400) // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        return f"{sign}{days} days, {hours} hours, {minutes} minutes, {seconds} seconds"

if __name__ == '__main__':
    anchor = datetime(2024, 6, 15, 10, 0, 0)
    later = datetime(2024, 6, 16, 12, 30, 45)
    earlier = datetime(2024, 6, 14, 8, 15, 0)
    
    diff = TimeDiffer(anchor)
    
    delta_later = diff.compute_delta(later)
    print(delta_later)
    
    seconds_later = diff.get_seconds(later)
    print(seconds_later)
    
    duration_later = diff.format_duration(later)
    print(duration_later)
    
    delta_earlier = diff.compute_delta(earlier)
    print(delta_earlier)
    
    seconds_earlier = diff.get_seconds(earlier)
    print(seconds_earlier)
    
    duration_earlier = diff.format_duration(earlier)
    print(duration_earlier)