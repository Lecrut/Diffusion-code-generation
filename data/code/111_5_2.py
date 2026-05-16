from datetime import date
def date_to_components(dt):
    year = dt.year
    day = dt.day
    day_of_week = dt.strftime("%A")
    return (year, day, day_of_week)
if __name__ == '__main__':
    sample_date = date(2023, 10, 26)
    result = date_to_components(sample_date)
    print(result)