from datetime import date
class DateConverter:
    def get_day_of_week(self, date_obj: date) -> int:
        if not isinstance(date_obj, date):
            raise TypeError("Input must be a datetime.date object.")
        return date_obj.weekday()
if __name__ == '__main__':
    converter = DateConverter()
    sample_dates = [
        date(2023, 1, 1),                                   
        date(2023, 1, 2),                                   
        date(2023, 12, 31),                                  
        date(2024, 5, 15)                                      
    ]
    print("Testing DateConverter.get_day_of_week:")
    for d in sample_dates:
        day_index = converter.get_day_of_week(d)
        print(f"Date: {d}, Day Index (Monday=0): {day_index}")
    try:
        converter.get_day_of_week("not_a_date")
    except TypeError as e:
        print(f"\nCaught expected error for invalid input: {e}")