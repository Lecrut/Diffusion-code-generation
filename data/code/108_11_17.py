class DateProcessor:
    DAY_OF_MONTH = "day"

    @staticmethod
    def get_day(date_obj):
        return date_obj.day

if __name__ == '__main__':
    import datetime
    target_date = datetime.date(2023, 3, 15)
    processor = DateProcessor()
    print(processor.get_day(target_date))