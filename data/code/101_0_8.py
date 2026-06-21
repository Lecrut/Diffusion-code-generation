import datetime

def compute_weekday(date_str):
    year, month, day = date_str.split("-")
    parsed_date = datetime.date(int(year), int(month), int(day))
    weekday_number = parsed_date.weekday()
    weekday_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return weekday_names[weekday_number]

if __name__ == '__main__':
    sample_date = "2023-10-05"
    result = compute_weekday(sample_date)
    print(result)