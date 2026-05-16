import datetime
def date_to_components(date_obj):
    year = date_obj.year
    day = date_obj.day
    day_of_week = date_obj.strftime('%A')
    return (year, day, day_of_week)
if __name__ == '__main__':
    sample_date = datetime.date(2023, 10, 26)
    result = date_to_components(sample_date)
    print(result)