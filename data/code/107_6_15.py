from datetime import date

def format_date_custom(d):
    if not isinstance(d, date):
        raise ValueError("Input must be a date instance")
    day_names = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
    month_names = ('January', 'February', 'March', 'April', 'May', 'June',
                   'July', 'August', 'September', 'October', 'November', 'December')
    day_name = day_names[d.weekday()]
    month_name = month_names[d.month - 1]
    return f"{day_name}, {month_name} {d.day:02d}, {d.year}"
if __name__ == '__main__':
    sample_date = date(2024, 1, 15)
    print(format_date_custom(sample_date))