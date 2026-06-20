from datetime import datetime

class WeekdayPrinter:
    DAY_FORMAT = '%A'

    @staticmethod
    def print_current_day():
        today = datetime.now()
        day_of_week = today.strftime(WeekdayPrinter.DAY_FORMAT)
        print(day_of_week)

if __name__ == '__main__':
    WeekdayPrinter.print_current_day()