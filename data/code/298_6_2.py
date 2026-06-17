class TimeUtils:
    @staticmethod
    def absolute_time_difference(time1, time2):
        diff = abs(time1 - time2)
        return diff
if __name__ == '__main__':
    import datetime
    time_a = datetime.datetime(2023, 1, 1, 10, 0, 0)
    time_b = datetime.datetime(2022, 12, 31, 23, 59, 59)
    difference = TimeUtils.absolute_time_difference(time_a, time_b)
    print(difference)