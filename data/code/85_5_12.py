import datetime

class DateDifferenceCalculator:
    WEEKS_PER_DAY = 7

    @staticmethod
    def date_to_ordinal(date_str):
        dt = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        return dt.toordinal()

    @classmethod
    def weeks_difference(cls, date1_str, date2_str):
        ordinal1 = cls.date_to_ordinal(date1_str)
        ordinal2 = cls.date_to_ordinal(date2_str)
        difference = abs(ordinal1 - ordinal2)
        return difference // cls.WEEKS_PER_DAY

if __name__ == '__main__':
    calculator = DateDifferenceCalculator()
    date_a = "2023-01-01"
    date_b = "2023-01-08"
    result = calculator.weeks_difference(date_a, date_b)
    print(result)