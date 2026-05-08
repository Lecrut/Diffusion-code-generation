class DateConverter:
    def get_day_of_week(self, date_object):
        if not isinstance(date_object, (datetime.date, datetime.datetime)):
            raise TypeError("Input must be a datetime.date or datetime.datetime object.")
        if isinstance(date_object, datetime.datetime):
            date_only = date_object.date()
        else:
            date_only = date_object
        return date_only.weekday()
if __name__ == '__main__':
    import datetime
    converter = DateConverter()
    sample_dates = [
        datetime.date(2023, 10, 2),          
        datetime.date(2023, 10, 1),          
        datetime.date(2023, 10, 31),          
        datetime.date(2024, 1, 1)           
    ]
    for date_obj in sample_dates:
        try:
            day_index = converter.get_day_of_week(date_obj)
            print(f"Date: {date_obj}, Day of Week (Monday=0): {day_index}")
        except TypeError as e:
            print(f"Error processing {date_obj}: {e}")