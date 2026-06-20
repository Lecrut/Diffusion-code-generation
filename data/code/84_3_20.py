from datetime import datetime

class DateParser:
    @staticmethod
    def is_valid_date(date_str):
        try:
            datetime.strptime(date_str, '%Y-%m-%d')
            return True
        except ValueError:
            return False
    
    @staticmethod
    def day_of_year(date_str):
        if not DateParser.is_valid_date(date_str):
            raise ValueError("Invalid date format")
        year, month, day = map(int, date_str.split('-'))
        return datetime(year, month, day).timetuple().tm_yday

if __name__ == '__main__':
    print(DateParser.day_of_year('2023-10-27'))