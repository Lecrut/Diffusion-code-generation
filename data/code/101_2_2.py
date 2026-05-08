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
    sample_date_2 = datetime.datetime(2023, 10, 31, 14, 30)
    sample_date_3 = datetime.date(2024, 1, 1)
    print(f"Date {sample_date_1}: Day of the week (Monday=0): {converter.get_day_of_week(sample_date_1)}")
    print(f"Date {sample_date_2}: Day of the week (Monday=0): {converter.get_day_of_week(sample_date_2)}")
    print(f"Date {sample_date_3}: Day of the week (Monday=0): {converter.get_day_of_week(sample_date_3)}")