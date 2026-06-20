class DateHelper:
    TARGET_YEAR = 2024

    @staticmethod
    def is_sunday(date):
        return date.weekday() == 6

    @classmethod
    def find_first_sunday_after_jan_1(cls):
        target_date = cls.TARGET_YEAR, 1, 1
        while not cls.is_sunday(target_date):
            target_date = (target_date[0], target_date[1] + 1) if target_date[1] < 12 else (target_date[0] + 1, 1)
        return target_date

if __name__ == '__main__':
    first_sunday = DateHelper.find_first_sunday_after_jan_1()
    print(f"First Sunday after January 1, {DateHelper.TARGET_YEAR}: {first_sunday}")