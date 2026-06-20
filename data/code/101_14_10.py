from datetime import date

def get_day_info(dt: date) -> tuple[str, int]:
    if not isinstance(dt, date):
        raise ValueError("Input must be a valid date object")
    
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day_name = days[dt.weekday()]
    day_number = dt.day
    return (day_name, day_number)

if __name__ == '__main__':
    sample_date = date(2025, 3, 15)
    result = get_day_info(sample_date)
    print(f"Date: {sample_date}, Day Name: {result[0]}, Day Number: {result[1]}")