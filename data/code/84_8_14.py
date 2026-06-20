import datetime

class DateProcessor:
    @staticmethod
    def calculate_day_of_year(date_str):
        date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        year_start = datetime.datetime(date_obj.year, 1, 1)
        day_of_year = (date_obj - year_start).days + 1
        return day_of_year

if __name__ == '__main__':
    processor = DateProcessor()
    date_str_1 = "2023-04-15"
    result_1 = processor.calculate_day_of_year(date_str_1)
    print(f"Date: {date_str_1}, Day of Year: {result_1}")
    date_str_2 = "2024-01-01"
    result_2 = processor.calculate_day_of_year(date_str_2)
    print(f"Date: {date_str_2}, Day of Year: {result_2}")