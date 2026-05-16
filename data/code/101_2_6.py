from datetime import date
class DateConverter:
    def get_day_of_week(self, date_obj: date) -> int:
        if not isinstance(date_obj, date):
            raise TypeError("Input must be a datetime.date object.")
        return date_obj.weekday()
if __name__ == '__main__':
    converter = DateConverter()
    date1 = date(2023, 10, 2)          
    date2 = date(2023, 10, 3)           
    date3 = date(2023, 10, 6)          
    date4 = date(2023, 10, 1)          
    print(f"Date: {date1}, Day of Week (Monday=0): {converter.get_day_of_week(date1)}")
    print(f"Date: {date2}, Day of Week (Monday=0): {converter.get_day_of_week(date2)}")
    print(f"Date: {date3}, Day of Week (Monday=0): {converter.get_day_of_week(date3)}")
    print(f"Date: {date4}, Day of Week (Monday=0): {converter.get_day_of_week(date4)}")