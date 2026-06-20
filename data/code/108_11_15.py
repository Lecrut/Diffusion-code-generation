import datetime

class DateHandler:
    DEFAULT_DATE = datetime.date(2023, 3, 15)

    @staticmethod
    def get_day_of_month(date_obj):
        try:
            return date_obj.day
        except AttributeError:
            return None

if __name__ == '__main__':
    handler = DateHandler()
    print(f"Day of month for {DateHandler.DEFAULT_DATE}: {handler.get_day_of_month(DateHandler.DEFAULT_DATE)}")