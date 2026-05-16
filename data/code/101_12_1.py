class DateConverter:
    def get_day_name(self, date_string):
        try:
            month, day, year = map(int, date_string.split('/'))
            import datetime
            date_obj = datetime.date(year, month, day)
            return date_obj.weekday()
        except ValueError:
            return -1
if __name__ == '__main__':
    converter = DateConverter()
    date1 = "01/15/2023"
    date2 = "12/31/2022"
    date3 = "02/28/2024"
    date4 = "13/01/2023"
    print(f"Date {date1}: {converter.get_day_name(date1)}")
    print(f"Date {date2}: {converter.get_day_name(date2)}")
    print(f"Date {date3}: {converter.get_day_name(date3)}")
    print(f"Date {date4}: {converter.get_day_name(date4)}")