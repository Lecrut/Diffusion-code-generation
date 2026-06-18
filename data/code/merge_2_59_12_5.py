import datetime
def get_day_name(date: datetime.date) -> str:
    if date.year < 1 or date.year > 9999:
        raise ValueError("Year must be between 1 and 9999.")
    day_names = [
        "Monday", "Tuesday", "Wednesday", "Thursday", 
        "Friday", "Saturday", "Sunday"
    ]
    return day_names[date.weekday()]
if __name__ == '__main__':
    sample_date = datetime.date(2023, 10, 5)
    print(get_day_name(sample_date))