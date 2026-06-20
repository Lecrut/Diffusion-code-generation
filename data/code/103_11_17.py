class TimeUtils:
    @staticmethod
    def seconds_since_midnight():
        now = datetime.datetime.now()
        midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
        return (now - midnight).total_seconds()

if __name__ == '__main__':
    time_utils = TimeUtils()
    elapsed_time = time_utils.seconds_since_midnight()
    print(elapsed_time)