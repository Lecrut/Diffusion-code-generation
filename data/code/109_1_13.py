class MonthRemaining:
    def __init__(self):
        from datetime import datetime
        self.today = datetime.now()

    @staticmethod
    def get_last_day_of_month(year, month):
        if month == 12:
            return year + 1, 1
        else:
            next_month = month + 1
            next_year = year
            return next_year, next_month

    def seconds_until_end_of_month(self, timestamp):
        from datetime import datetime, timedelta
        dt = datetime.fromtimestamp(timestamp)
        target_year, target_month = self.get_last_day_of_month(dt.year, dt.month)
        last_day = datetime(target_year, target_month, 1) - timedelta(days=1)
        return (last_day - dt).total_seconds()

if __name__ == '__main__':
    m = MonthRemaining()
    sample_timestamp = 1672531200
    print(m.seconds_until_end_of_month(sample_timestamp))