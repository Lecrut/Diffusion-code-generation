import datetime

class DateDecorator:
    DAY_NAMES = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    @staticmethod
    def prepend_day_name(date_obj):
        return f"{DateDecorator.DAY_NAMES[date_obj.weekday()]} {date_obj}"

if __name__ == '__main__':
    sample_date_today = datetime.date.today()
    sample_date_monday = datetime.date(2023, 10, 23)
    sample_date_saturday = datetime.date(2023, 10, 28)

    result_today = DateDecorator.prepend_day_name(sample_date_today)
    print(f"Today's date with day name: {result_today}")

    result_monday = DateDecorator.prepend_day_name(sample_date_monday)
    print(f"Monday's date with day name: {result_monday}")

    result_saturday = DateDecorator.prepend_day_name(sample_date_saturday)
    print(f"Saturday's date with day name: {result_saturday}")