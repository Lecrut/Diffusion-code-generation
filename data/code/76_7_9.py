from datetime import datetime, timedelta

class DateUtils:
    @staticmethod
    def calculate_previous_date(days):
        return (datetime.now() - timedelta(days=days)).strftime('%Y-%m-%d')

if __name__ == '__main__':
    print(DateUtils.calculate_previous_date(5))