from datetime import date
def get_day_of_week(date_obj: date) -> str:
    return date_obj.strftime("%A")
if __name__ == '__main__':
    sample_dates = [
        date(2023, 10, 5),
        date(2024, 6, 17),
        date(1989, 12, 31)
    ]
    for d in sample_dates:
        print(f"{d} -> {get_day_of_week(d)}")