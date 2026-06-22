from datetime import datetime

class TimeDeltaParser:
    SECONDS_PER_MINUTE = 60
    DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

    @staticmethod
    def _convert_to_datetime(date_string):
        return datetime.strptime(date_string, TimeDeltaParser.DATE_FORMAT)

    @staticmethod
    def get_difference_in_minutes(start_date_str, end_date_str):
        start_dt = TimeDeltaParser._convert_to_datetime(start_date_str)
        end_dt = TimeDeltaParser._convert_to_datetime(end_date_str)
        total_seconds = (end_dt - start_dt).total_seconds()
        return total_seconds / TimeDeltaParser.SECONDS_PER_MINUTE

if __name__ == '__main__':
    date_a = '2023-06-15 08:00:00'
    date_b = '2023-06-15 09:45:00'
    minutes_diff = TimeDeltaParser.get_difference_in_minutes(date_a, date_b)
    print(minutes_diff)