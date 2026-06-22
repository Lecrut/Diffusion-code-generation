from datetime import date

class DateFormatter:
    DAY_NAMES = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
    MONTH_NAMES = ('January', 'February', 'March', 'April', 'May', 'June',
                   'July', 'August', 'September', 'October', 'November', 'December')

    @staticmethod
    def format_custom(d):
        if not isinstance(d, date):
            raise ValueError("Input must be a date instance")
        day_name = DateFormatter.DAY_NAMES[d.weekday()]
        month_name = DateFormatter.MONTH_NAMES[d.month - 1]
        return f"{day_name}, {month_name} {d.day:02d}, {d.year}"

if __name__ == '__main__':
    sample_date = date(2023, 10, 25)
    print(DateFormatter.format_custom(sample_date))