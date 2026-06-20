class DateFinder:
    TARGET_YEAR = 2024

    @staticmethod
    def is_sunday(date):
        return date.weekday() == 6

    @classmethod
    def find_first_sunday_after_jan_1(cls):
        target_date = cls.TARGET_YEAR, 1, 1
        while True:
            current_date = datetime.date(*target_date)
            if cls.is_sunday(current_date):
                return current_date
            target_date = (current_date.year, current_date.month, current_date.day + 1)

if __name__ == '__main__':
    first_sunday = DateFinder.find_first_sunday_after_jan_1()
    print(first_sunday)