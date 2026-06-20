import time

class TimeCalculator:
    def get_elapsed_seconds_today(self):
        local_time = time.localtime()
        start_of_day = time.struct_time((local_time.tm_year, local_time.tm_mon, local_time.tm_mday, 0, 0, 0, local_time.tm_wday, local_time.tm_yday, local_time.tm_isdst))
        elapsed_seconds = (time.mktime(local_time) - time.mktime(start_of_day))
        return int(elapsed_seconds)

if __name__ == '__main__':
    calculator = TimeCalculator()
    print(f"Elapsed seconds today: {calculator.get_elapsed_seconds_today()}")