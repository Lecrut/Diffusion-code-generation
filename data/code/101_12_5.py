class DateConverter:
    def get_day_name(self, date_string):
        try:
            month, day, year = date_string.split('/')
            month_num = int(month)
            day_num = int(day)
            year_num = int(year)
            import datetime
            date_obj = datetime.date(year_num, month_num, day_num)
            return date_obj.weekday()
        except ValueError:
            return -1
if __name__ == '__main__':
    converter = DateConverter()
    date1 = "10/25/2023"
    date2 = "01/01/2024"
    date3 = "12/31/2022"
    date4 = "02/29/2024"
    date5 = "13/40/2023"
    print(f"Date: {date1}, Day Index: {converter.get_day_name(date1)}")
    print(f"Date: {date2}, Day Index: {converter.get_day_name(date2)}")
    print(f"Date: {date3}, Day Index: {converter.get_day_name(date3)}")
    print(f"Date: {date4}, Day Index: {converter.get_day_name(date4)}")
    print(f"Date: {date5}, Day Index: {converter.get_day_name(date5)}")