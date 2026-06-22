class DateExtractor:
    DAY_OF_MONTH = 2

    @staticmethod
    def get_day(date_obj):
        if not hasattr(date_obj, 'day'):
            raise ValueError("Input must have a day attribute")
        return date_obj.day

if __name__ == '__main__':
    import datetime
    target_date = datetime.date(2023, 3, 15)
    extractor = DateExtractor()
    day_value = extractor.get_day(target_date)
    print(day_value)