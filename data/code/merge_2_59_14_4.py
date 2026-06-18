import datetime
def get_day_of_week(date_obj: datetime.date) -> str:
    return date_obj.strftime("%A")
class DateFormatter:
    def __init__(self):
        self.custom_formats = {
            "short": "%a, %d %b",
            "long": "%B %d, %Y (%A)",
            "iso": "%Y-%m-%d"
        }
    def format_date(self, date_obj: datetime.date, fmt_key: str | None = None) -> str:
        if fmt_key is not None and fmt_key in self.custom_formats:
            return date_obj.strftime(self.custom_formats[fmt_key])
        else:
            return get_day_of_week(date_obj)
if __name__ == '__main__':
    formatter = DateFormatter()
    sample_dates = [
        datetime.date(2023, 10, 5),
        datetime.datetime.now().date(),
        datetime.date(1970, 1, 1)
    ]
    print("Day of Week and Custom Formats:\n")
    for date in sample_dates:
        day_name = formatter.format_date(date)
        if hasattr(formatter.custom_formats.get('short'), 'format'):                                                                                  
            short_str = formatter.format_date(date, "short")
            long_str = formatter.format_date(date, "long")
            iso_str = formatter.format_date(date, "iso")
        print(f"Date: {date}")
        print(f"Full Name: {day_name}\nShort Format: {short_str}, Long Format: {long_str}, ISO Format: {iso_str}\n")