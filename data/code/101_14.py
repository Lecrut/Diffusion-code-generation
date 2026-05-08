from datetime import date
def get_day_info(dt: date) -> tuple[str, int]:
    day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day_index = dt.weekday()
    day_name = day_names[day_index]
    day_number = day_index + 1
    return (day_name, day_number)
if __name__ == '__main__':
    sample_dates = [
        date(2023, 10, 25),
        date(2023, 1, 1),
        date(2024, 12, 25),
        date(2024, 1, 1)
    ]
    for d in sample_dates:
        name, number = get_day_info(d)
        print(f"Date: {d}, Day Name: {name}, Day Number: {number}")