from datetime import date
def format_date(date_obj):
    month_name = date_obj.strftime('%B')
    day = date_obj.day
    year = date_obj.year
    return f"{month_name} {day}, {year}"
if __name__ == '__main__':
    sample_date1 = date(2023, 1, 1)
    sample_date2 = date(2024, 5, 15)
    print(format_date(sample_date1))
    print(format_date(sample_date2))