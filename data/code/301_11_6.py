from datetime import date
def format_date(date_obj):
    month_name = date_obj.strftime("%B")
    day = date_obj.day
    year = date_obj.year
    return f"{month_name} {day}, {year}"
if __name__ == '__main__':
    sample_date1 = date(2023, 1, 1)
    formatted_date1 = format_date(sample_date1)
    print(f"Input: {sample_date1}")
    print(f"Output: {formatted_date1}")
    sample_date2 = date(2024, 5, 15)
    formatted_date2 = format_date(sample_date2)
    print(f"Input: {sample_date2}")
    print(f"Output: {formatted_date2}")
    sample_date3 = date(1999, 12, 31)
    formatted_date3 = format_date(sample_date3)
    print(f"Input: {sample_date3}")
    print(f"Output: {formatted_date3}")