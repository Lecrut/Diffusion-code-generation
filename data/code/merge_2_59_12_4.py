import datetime
def get_day_name(date_obj: datetime.date) -> str:
    if date_obj.year < 1 or date_obj.year > 9999:
        raise ValueError("Year must be between 1 and 9999.")
    try:
        day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        return day_names[date_obj.weekday()]
    except Exception as e:
        raise ValueError(f"Invalid date input. Error details: {e}")
if __name__ == '__main__':
    sample_date = datetime.date(2023, 10, 5)
    try:
        result = get_day_name(sample_date)
        print(result)
    except ValueError as ve:
        print(f"Error: {ve}")