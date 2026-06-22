import datetime

def compute_weekday(date_string):
    parsed_date = datetime.datetime.strptime(date_string, "%Y-%m-%d").date()
    weekday_number = parsed_date.weekday()
    day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return day_names[weekday_number]

if __name__ == '__main__':
    sample_date = "2023-10-05"
    day_of_week = compute_weekday(sample_date)
    print(day_of_week)