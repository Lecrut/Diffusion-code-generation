from datetime import date
def get_day_info(dt: date) -> tuple[str, int]:
    day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day_index = dt.weekday()
    day_name = day_names[day_index]
    day_number = day_index + 1
    return (day_name, day_number)
if __name__ == '__main__':
    sample_date_1 = date(2023, 10, 25)
    sample_date_2 = date(2024, 1, 1)
    sample_date_3 = date(2023, 12, 31)
    result1 = get_day_info(sample_date_1)
    print(f"Date: {sample_date_1}, Result: {result1}")
    result2 = get_day_info(sample_date_2)
    print(f"Date: {sample_date_2}, Result: {result2}")
    result3 = get_day_info(sample_date_3)
    print(f"Date: {sample_date_3}, Result: {result3}")