import datetime
def manipulate_date(date_obj, year, month, day):
    new_date = date_obj.replace(year=year, month=month, day=day)
    return new_date
if __name__ == '__main__':
    original_date = datetime.date(2023, 10, 26)
    print(f"Original Date: {original_date}")
    new_year = 2024
    new_month = 1
    new_day = 15
    modified_date = manipulate_date(original_date, new_year, new_month, new_day)
    print(f"Manipulated Date (Year={new_year}, Month={new_month}, Day={new_day}): {modified_date}")