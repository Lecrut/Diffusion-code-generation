from datetime import datetime

class TimeUtils:
    @staticmethod
    def elapsed_minutes_since_midnight(dt: datetime) -> int:
        midnight = dt.replace(hour=0, minute=0, second=0, microsecond=0)
        return (dt - midnight).seconds // 60

if __name__ == '__main__':
    sample_dt = datetime(2023, 10, 5, 14, 30, 0)
    print(TimeUtils.elapsed_minutes_since_midnight(sample_dt))