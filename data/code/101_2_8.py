class DateConverter:
    def get_day_of_week(self, date_object):
        if not isinstance(date_object, (datetime.date, datetime.datetime)):
            raise TypeError("Input must be a datetime.date or datetime.datetime object.")
        day_of_week = date_object.weekday()
        return day_of_week
if __name__ == '__main__':
    import datetime
    converter = DateConverter()
    sample_date_1 = datetime.date(2023, 10, 2)
    day1 = converter.get_day_of_week(sample_date_1)
    print(f"Date: {sample_date_1}, Day of Week (Monday=0): {day1}")
    sample_date_2 = datetime.date(2023, 10, 29)
    day2 = converter.get_day_of_week(sample_date_2)
    print(f"Date: {sample_date_2}, Day of Week (Monday=0): {day2}")
    sample_date_3 = datetime.date(2023, 10, 4)
    day3 = converter.get_day_of_week(sample_date_3)
    print(f"Date: {sample_date_3}, Day of Week (Monday=0): {day3}")
    sample_date_4 = datetime.date(2023, 10, 6)
    day4 = converter.get_day_of_week(sample_date_4)
    print(f"Date: {sample_date_4}, Day of Week (Monday=0): {day4}")