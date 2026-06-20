import datetime

class DateProcessor:
    WEEKDAY_MAP = {
        0: "MONDAY",
        1: "TUESDAY",
        2: "WEDNESDAY",
        3: "THURSDAY",
        4: "FRIDAY",
        5: "SATURDAY",
        6: "SUNDAY"
    }

    @staticmethod
    def get_weekday(date_str):
        try:
            day, month, year = map(int, date_str.split('-'))
            date_obj = datetime.date(year, month, day)
            weekday_num = date_obj.weekday()
            return DateProcessor.WEEKDAY_MAP[weekday_num]
        except ValueError:
            raise ValueError("Invalid date components provided.")

if __name__ == '__main__':
    sample_date = "04-07-2024"
    processor = DateProcessor()
    print(processor.get_weekday(sample_date))