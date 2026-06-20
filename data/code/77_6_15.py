from datetime import datetime

class TimeHelper:
    @staticmethod
    def elapsed_minutes_since_midnight(dt):
        midnight = dt.replace(hour=0, minute=0, second=0, microsecond=0)
        return (dt - midnight).total_seconds() // 60

if __name__ == '__main__':
    sample_dt = datetime(2023, 10, 5, 14, 30, 0)
    helper = TimeHelper()
    print(helper.elapsed_minutes_since_midnight(sample_dt))