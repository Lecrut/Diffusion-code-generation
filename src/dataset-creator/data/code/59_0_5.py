from datetime import datetime
def get_day_of_week(date_string: str) -> int:
    date_obj = datetime.strptime(date_string, "%Y-%m-%d")
    return date_obj.weekday()
if __name__ == '__main__':
    test_dates = [
        "2023-10-05",
        "2024-07-20"
    ]
    for d in test_dates:
        day_index = get_day_of_week(d)
        print(f"{d} is a {['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][day_index]}")