from datetime import datetime, timedelta

class TimeCalculator:
    def get_duration_components(self, t_start: datetime, t_end: datetime):
        if not isinstance(t_start, datetime) or not isinstance(t_end, datetime):
            raise ValueError("Arguments must be datetime instances")
        
        if t_end < t_start:
            delta_seconds = abs((t_start - t_end).total_seconds())
        else:
            delta_seconds = (t_end - t_start).total_seconds()
        
        days = int(delta_seconds // 86400)
        remainder_after_days = delta_seconds % 86400
        hours = int(remainder_after_days // 3600)
        remainder_after_hours = remainder_after_days % 3600
        minutes = int(remainder_after_hours // 60)
        seconds = int(remainder_after_hours % 60)
        
        return {
            "days": days,
            "hours": hours,
            "minutes": minutes,
            "seconds": seconds
        }

if __name__ == '__main__':
    calc = TimeCalculator()
    initial_time = datetime(2024, 6, 15, 8, 30, 0)
    final_time = datetime(2024, 6, 20, 17, 45, 30)
    
    result = calc.get_duration_components(initial_time, final_time)
    
    print(f"Days: {result['days']}")
    print(f"Hours: {result['hours']}")
    print(f"Minutes: {result['minutes']}")
    print(f"Seconds: {result['seconds']}")