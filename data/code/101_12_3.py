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
    date1 = "10/27/2023"
    date2 = "01/01/2024"
    date3 = "12/31/2022"
    date4 = "02/29/2024"
    date5 = "99/99/9999"
    print(f"Date {date1}: {converter.get_day_name(date1)}")
    print(f"Date {date2}: {converter.get_day_name(date2)}")
    print(f"Date {date3}: {converter.get_day_name(date3)}")
    print(f"Date {date4}: {converter.get_day_name(date4)}")
    print(f"Date {date5}: {converter.get_day_name(date5)}")