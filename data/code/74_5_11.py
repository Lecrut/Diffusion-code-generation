from datetime import date

class WeekdayService:
    def __init__(self):
        self.days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    def get_day_name(self, date_obj):
        return self.days[date_obj.weekday()]

if __name__ == '__main__':
    service = WeekdayService()
    date1 = date(2023, 10, 25)
    print(f"Date: {date1}, Day of the week: {service.get_day_name(date1)}")
    date2 = date(2024, 1, 1)
    print(f"Date: {date2}, Day of the week: {service.get_day_name(date2)}")
    date3 = date(2025, 12, 25)
    print(f"Date: {date3}, Day of the week: {service.get_day_name(date3)}")
    date4 = date(2023, 5, 10)
    print(f"Date: {date4}, Day of the week: {service.get_day_name(date4)}")