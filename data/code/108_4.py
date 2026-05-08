from datetime import date
def format_date(date_obj):
    day = date_obj.day
    month = date_obj.month
    return f"Day {day} of Month {month}"
if __name__ == '__main__':
    sample_date = date(2023, 10, 15)
    result = format_date(sample_date)
    print(result)