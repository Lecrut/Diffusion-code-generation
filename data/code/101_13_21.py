import datetime

def compute_weekday(year, month, day):
    date_instance = datetime.date(year, month, day)
    weekday_number = date_instance.weekday()
    full_name = date_instance.strftime('%A')
    return full_name.upper()

if __name__ == '__main__':
    sample_year = 2024
    sample_month = 7
    sample_day = 4
    computed_result = compute_weekday(sample_year, sample_month, sample_day)
    print(computed_result)