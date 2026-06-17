import datetime
def subtract_years(date_obj: datetime.date, years_to_subtract: int) -> datetime.date:
    return date_obj.replace(year=date_obj.year - years_to_subtract)
if __name__ == '__main__':
    sample_date = datetime.date(2013, 4, 15)
    year_difference = 67
    new_date = subtract_years(sample_date, year_difference)
    print(new_date.strftime("%Y-%m-%d"))