from datetime import datetime

def format_date_custom(date_obj):
    if not isinstance(date_obj, datetime):
        raise ValueError("Input must be a datetime instance")
    day_names = (
        "Monday", "Tuesday", "Wednesday", "Thursday",
        "Friday", "Saturday", "Sunday"
    )
    month_names = (
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    )
    day_name = day_names[date_obj.weekday()]
    month_name = month_names[date_obj.month - 1]
    return f"{day_name}, {month_name} {date_obj.day:02d}, {date_obj.year}"

if __name__ == '__main__':
    sample_date = datetime(2023, 10, 25)
    result = format_date_custom(sample_date)
    print(result)