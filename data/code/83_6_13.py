from datetime import date

class DatePairComparer:
    @staticmethod
    def are_dates_equal(date1, date2):
        return date1 == date2
    
    @classmethod
    def compare_date_pairs(cls, dates):
        for i in range(len(dates) - 1):
            if cls.are_dates_equal(dates[i], dates[i + 1]):
                yield True

if __name__ == '__main__':
    sample_dates = [date(2023, 10, 27), date(2023, 10, 27), date(2023, 11, 27)]
    comparer = DatePairComparer()
    for result in comparer.compare_date_pairs(sample_dates):
        print(result)