import datetime

def compute_weekday(year, month, day):
    date_instance = datetime.date(year, month, day)
    weekday_name = date_instance.strftime('%A')
    return weekday_name.upper()

if __name__ == '__main__':
    sample_year = 2024
    sample_month = 7
    sample_day = 4
    output = compute_weekday(sample_year, sample_month, sample_day)
    print(output)