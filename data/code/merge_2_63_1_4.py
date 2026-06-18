from datetime import timedelta, date
def add_years(date: date, years: int) -> date:
    return date + timedelta(days=years * 365 + (date.timetuple().tm_yday - 1))
if __name__ == '__main__':
    start_date = date(2023, 1, 15)
    years_to_add = 5
    result = add_years(start_date, years_to_add)
    print(result)