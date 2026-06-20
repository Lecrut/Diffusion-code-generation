import datetime

class DateCalculator:
    def calculate_difference(self, date1_str, date2_str):
        date_format = '%Y-%m-%d'
        date1 = datetime.datetime.strptime(date1_str, date_format)
        date2 = datetime.datetime.strptime(date2_str, date_format)
        difference = abs(date2 - date1)
        return difference

if __name__ == '__main__':
    calculator = DateCalculator()
    sample_date1 = "2023-04-01"
    sample_date2 = "2023-04-15"
    result = calculator.calculate_difference(sample_date1, sample_date2)
    print(result)