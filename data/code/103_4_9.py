import datetime

class TimeFraction:
    def __init__(self):
        self.current_time = datetime.datetime.now()

    def get_fractional_day(self):
        return (self.current_time - datetime.datetime.combine(datetime.date.today(), datetime.time.min)).total_seconds()

if __name__ == '__main__':
    time_fraction_instance = TimeFraction()
    fractional_day_seconds = time_fraction_instance.get_fractional_day()
    print(fractional_day_seconds)