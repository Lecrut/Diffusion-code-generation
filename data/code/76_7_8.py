from datetime import datetime, timedelta

class DateUtils:
    @staticmethod
    def calculate_date(days):
        return datetime.now() + timedelta(days=days)

if __name__ == '__main__':
    result = DateUtils.calculate_date(5)
    print(result)