import datetime

DAY_NAMES = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

def get_weekday_name(date_string):
    parsed_date = datetime.datetime.strptime(date_string, "%Y-%m-%d").date()
    return DAY_NAMES[parsed_date.weekday()]

if __name__ == '__main__':
    sample_date = "2023-10-05"
    weekday = get_weekday_name(sample_date)
    print(weekday)