from datetime import date

def get_day_name(date_obj):
    days = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday"
    }
    return days[date_obj.weekday()]

if __name__ == '__main__':
    sample_dates = [
        date(2023, 10, 25),
        date(2023, 1, 1),
        date(2024, 12, 25),
        date(2025, 5, 10)
    ]
    
    for sample_date in sample_dates:
        print(f"Date: {sample_date}, Day of the week: {get_day_name(sample_date)}")