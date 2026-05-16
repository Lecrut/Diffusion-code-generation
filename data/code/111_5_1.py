import datetime
def date_to_components(date_obj):
    year = date_obj.year
    day = date_obj.day
    day_of_week = date_obj.strftime("%A")
    return (year, day, day_of_week)
if __name__ == '__main__':
    sample_date_str = "2023-10-27"
    date_obj = datetime.datetime.strptime(sample_date_str, "%Y-%m-%d").date()
    result = date_to_components(date_obj)
    print(result)