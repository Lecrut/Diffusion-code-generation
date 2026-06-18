from datetime import date
def get_day_of_week(date_obj: date) -> str:
    return date_obj.strftime("%A")
if __name__ == '__main__':
    sample_dates = [date(2023, 10, 5), date(2024, 6, 15), date(2025, 12, 31)]
    for d in sample_dates:
        day_name = get_day_of_week(d)
        print(f"{d} is a {day_name}")