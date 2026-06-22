import datetime

class DayOfWeekResolver:
    DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    MONTHS = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]

    @staticmethod
    def _parse_date(date_string):
        parts = date_string.split("-")
        year = int(parts[0])
        month = int(parts[1])
        day = int(parts[2])
        return datetime.date(year, month, day)

    @staticmethod
    def resolve(date_string):
        date_obj = DayOfWeekResolver._parse_date(date_string)
        return DayOfWeekResolver.DAYS[date_obj.weekday()]

if __name__ == '__main__':
    target = "2023-10-05"
    day_name = DayOfWeekResolver.resolve(target)
    print(day_name)