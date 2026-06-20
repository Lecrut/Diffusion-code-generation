class TimeUtils:
    @staticmethod
    def get_seconds_left_in_month(timestamp):
        from datetime import datetime, timedelta

        dt = datetime.fromtimestamp(timestamp)
        year, month = dt.year, dt.month
        if month == 12:
            next_month_year, next_month_day = year + 1, 1
        else:
            next_month_year, next_month_day = year, month + 1

        first_day_of_next_month = datetime(next_month_year, next_month_day, 1)
        last_day_of_current_month = first_day_of_next_month - timedelta(days=1)

        return (last_day_of_current_month - dt).total_seconds()

if __name__ == '__main__':
    sample_timestamp = 1672531200
    time_utils = TimeUtils()
    print(time_utils.get_seconds_left_in_month(sample_timestamp))