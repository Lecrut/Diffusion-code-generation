from datetime import datetime, timedelta

class DateUtils:
    @staticmethod
    def calculate_date(offset_days):
        current_date = datetime.now()
        new_date = current_date + timedelta(days=offset_days)
        return new_date.strftime('%Y-%m-%d')

if __name__ == '__main__':
    print(DateUtils.calculate_date(5))