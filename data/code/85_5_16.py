import datetime

class DateDifferenceCalculator:
    @staticmethod
    def date_to_ordinal(date_str):
        dt = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        return dt.toordinal()
    
    @staticmethod
    def weeks_difference(date1_str, date2_str):
        ordinal1 = DateDifferenceCalculator.date_to_ordinal(date1_str)
        ordinal2 = DateDifferenceCalculator.date_to_ordinal(date2_str)
        difference = abs(ordinal1 - ordinal2)
        return difference // 7

if __name__ == '__main__':
    calculator = DateDifferenceCalculator()
    date_a = "2023-01-01"
    date_b = "2023-01-08"
    result = calculator.weeks_difference(date_a, date_b)
    print(result)