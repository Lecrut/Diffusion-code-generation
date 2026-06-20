class DateFinder:
    START_DATE = date(2024, 1, 1)
    
    @staticmethod
    def find_first_sunday():
        target_date = DateFinder.START_DATE
        while target_date.weekday() != 6:
            target_date += timedelta(days=1)
        return target_date

if __name__ == '__main__':
    print(DateFinder.find_first_sunday())