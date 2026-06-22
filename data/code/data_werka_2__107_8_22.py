import datetime

class DateTimeFormatter:
    def __init__(self, dt_obj):
        if not isinstance(dt_obj, datetime.datetime):
            raise ValueError("Input must be a datetime object")
        self.dt = dt_obj

    def format_localized(self):
        day = self.dt.day
        month = self.dt.month
        year = self.dt.year
        hour = self.dt.hour
        minute = self.dt.minute
        period = "AM"
        if hour >= 12:
            period = "PM"
        display_hour = hour % 12
        if display_hour == 0:
            display_hour = 12
        day_str = f"{day:02d}"
        month_str = f"{month:02d}"
        hour_str = f"{display_hour:02d}"
        minute_str = f"{minute:02d}"
        return f"{day_str}/{month_str}/{year} {hour_str}:{minute_str} {period}"

    def get_date_string(self):
        return f"{self.dt.day}/{self.dt.month}/{self.dt.year}"

if __name__ == '__main__':
    sample_dt = datetime.datetime(2023, 10, 5, 14, 30, 0)
    formatter = DateTimeFormatter(sample_dt)
    print(formatter.format_localized())
    print(formatter.get_date_string())