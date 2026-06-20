import time

class TimeProcessor:
    def get_current_day_of_month(self):
        current_time = time.localtime()
        return current_time.tm_mday

if __name__ == '__main__':
    processor = TimeProcessor()
    print(processor.get_current_day_of_month())