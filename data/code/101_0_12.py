import datetime

def calculate_weekday(date_string):
    parsed_date = datetime.datetime.strptime(date_string, "%Y-%m-%d").date()
    weekday_number = parsed_date.weekday()
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days_of_week[weekday_number]

if __name__ == '__main__':
    sample_date = "2023-10-05"
    computed_day = calculate_weekday(sample_date)
    print(computed_day)