import datetime
def get_day_name(year: int, month: int, day: int) -> str:
    if year < 1 or year > 9999:
        raise ValueError("Year must be between 1 and 9999.")
    try:
        date_obj = datetime.date(year, month, day)
        days_map = {
            0: "Monday",
            1: "Tuesday",
            2: "Wednesday",
            3: "Thursday",
            4: "Friday",
            5: "Saturday",
            6: "Sunday"
        }
        return days_map[date_obj.weekday()]
    except ValueError as e:
        raise ValueError(f"Invalid date provided. {e}")
if __name__ == '__main__':
    sample_year = 2023
    sample_month = 10
    sample_day = 5
    try:
        day_name = get_day_name(sample_year, sample_month, sample_day)
        print(day_name)
    except ValueError as ve:
        print(f"Error: {ve}")