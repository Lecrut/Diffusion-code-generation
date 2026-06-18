from datetime import date
def get_weekday_name(date_obj: date) -> str:
    return date_obj.strftime("%A")
if __name__ == '__main__':
    sample_dates = [date(2023, 1, 1), date(2024, 6, 15), date(2025, 12, 25)]
    for d in sample_dates:
        print(f"{d} -> {get_weekday_name(d)}")