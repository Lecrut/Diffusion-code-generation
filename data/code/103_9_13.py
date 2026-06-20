import datetime

class TimeUtils:
    @staticmethod
    def get_elapsed_time_since_midnight():
        now = datetime.datetime.now()
        midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
        elapsed_time = now - midnight
        return elapsed_time

if __name__ == '__main__':
    elapsed_time = TimeUtils.get_elapsed_time_since_midnight()
    print(f"Elapsed time since midnight: {elapsed_time}")