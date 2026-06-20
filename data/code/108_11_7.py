import datetime

class DateUtil:
    DATE_FORMAT = "%Y-%m-%d"
    
    @staticmethod
    def get_day_of_month(date_str):
        try:
            date_obj = datetime.datetime.strptime(date_str, DateUtil.DATE_FORMAT).date()
            return date_obj.day
        except (ValueError, AttributeError):
            return None

if __name__ == '__main__':
    date_input = "2023-03-15"
    print(f"Day of month for {date_input}: {DateUtil.get_day_of_month(date_input)}")