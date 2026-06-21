from dateutil.parser import parse

class DateExtractor:
    WEEKDAY_MAP = {
        0: 'Monday',
        1: 'Tuesday',
        2: 'Wednesday',
        3: 'Thursday',
        4: 'Friday',
        5: 'Saturday',
        6: 'Sunday'
    }

    @staticmethod
    def get_day_from_string(date_str: str) -> str:
        parsed_date = parse(date_str)
        weekday_index = parsed_date.weekday()
        return DateExtractor.WEEKDAY_MAP[weekday_index]

if __name__ == '__main__':
    sample_date = 'January 15, 2023'
    day_of_week = DateExtractor.get_day_from_string(sample_date)
    print(day_of_week)