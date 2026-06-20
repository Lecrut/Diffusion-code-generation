from datetime import datetime

class DateUtil:
    @staticmethod
    def is_valid_date(date_str):
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return True
        except ValueError:
            return False

    @staticmethod
    def calculate_days_between(date1_str, date2_str):
        if not (DateUtil.is_valid_date(date1_str) and DateUtil.is_valid_date(date2_str)):
            raise ValueError("Invalid date format. Please use YYYY-MM-DD.")
        
        date1 = datetime.strptime(date1_str, "%Y-%m-%d")
        date2 = datetime.strptime(date2_str, "%Y-%m-%d")
        time_difference = abs(date2 - date1)
        return time_difference.days

if __name__ == '__main__':
    date_a = "2023-01-15"
    date_b = "2023-05-20"
    days = DateUtil.calculate_days_between(date_a, date_b)
    print(days)