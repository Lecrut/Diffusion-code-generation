from datetime import datetime

class DateFormatter:
    def format_rfc2822(self, date_obj):
        return date_obj.strftime('%a, %d %b %Y %H:%M:%S %z')

if __name__ == '__main__':
    formatter = DateFormatter()
    sample_date1 = datetime(2023, 4, 15)
    sample_date2 = datetime(2023, 12, 25)
    print(formatter.format_rfc2822(sample_date1))
    print(formatter.format_rfc2822(sample_date2))