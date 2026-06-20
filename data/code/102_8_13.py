from datetime import datetime

def is_weekday(iso_date_str):
    date_obj = datetime.strptime(iso_date_str, "%Y-%m-%d").date()
    day_index = date_obj.weekday()
    return day_index < 5

if __name__ == '__main__':
    sample_dates = [
        "2023-10-25",
        "2023-10-28",
        "2023-10-29",
        "2023-10-30"
    ]
    
    for date_str in sample_dates:
        print(f"Date: {date_str}, Is weekday: {is_weekday(date_str)}")