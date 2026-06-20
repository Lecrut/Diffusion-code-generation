import datetime

class DateHelper:
    def validate_date(self, year, month, day):
        try:
            datetime.date(year, month, day)
        except ValueError as e:
            raise ValueError(f"Invalid date: {e}")

    def get_day_of_week(self, year, month, day):
        self.validate_date(year, month, day)
        return datetime.date(year, month, day).weekday()

if __name__ == '__main__':
    date_helper = DateHelper()
    print(date_helper.get_day_of_week(2024, 7, 4))