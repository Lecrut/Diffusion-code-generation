from datetime import date

class DateExtractor:
    DAY_OF_MONTH = "day"

    @staticmethod
    def get_day(date_instance):
        if not isinstance(date_instance, date):
            raise ValueError("Input must be a date object")
        return date_instance.day

if __name__ == '__main__':
    target_date = date(2023, 3, 15)
    extractor = DateExtractor()
    day_value = extractor.get_day(target_date)
    print(day_value)