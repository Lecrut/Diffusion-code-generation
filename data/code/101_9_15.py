from datetime import datetime

class DayOfWeekCalculator:
    DATE_FORMAT = "%Y-%m-%d"
    
    @staticmethod
    def parse_date(date_string):
        return datetime.strptime(date_string, DayOfWeekCalculator.DATE_FORMAT)
    
    @staticmethod
    def get_day_upper(date_string):
        dt = DayOfWeekCalculator.parse_date(date_string)
        return dt.strftime("%A").upper()

if __name__ == '__main__':
    target_date = "2023-11-11"
    result = DayOfWeekCalculator.get_day_upper(target_date)
    print(result)