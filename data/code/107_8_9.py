from datetime import datetime
import locale

def format_datetime(dt: datetime) -> str:
    original_locale = locale.getlocale(locale.LC_TIME)
    try:
        locale.setlocale(locale.LC_TIME, '')
        formatted = dt.strftime('%d/%m/%Y %I:%M %p')
        return formatted
    finally:
        locale.setlocale(locale.LC_TIME, original_locale)

if __name__ == '__main__':
    sample_dt = datetime(2023, 10, 5, 14, 30, 0)
    result = format_datetime(sample_dt)
    print(result)