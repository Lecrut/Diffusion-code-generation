import datetime

class DayNamePrepender:
    DAY_NAMES = [
        "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
    ]

    @staticmethod
    def prepend_day_name(date_obj):
        return f"{DayNamePrepender.DAY_NAMES[date_obj.weekday()]} {date_obj}"

if __name__ == '__main__':
    sample_date_today = datetime.date.today()
    print(DayNamePrepender.prepend_day_name(sample_date_today))