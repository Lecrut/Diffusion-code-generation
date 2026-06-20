from datetime import date

def get_day_info(dt: date) -> str:
    day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return day_names[dt.weekday()]

if __name__ == '__main__':
    sample_date = date(2025, 3, 15)
    result = get_day_info(sample_date)
    print(f"Date: {sample_date}, Day Name: {result}")