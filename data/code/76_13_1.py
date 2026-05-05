import datetime
class DateCalculator:
    def get_difference(self, date1_str, date2_str):
        date1 = datetime.datetime.strptime(date1_str, "%Y-%m-%d")
        date2 = datetime.datetime.strptime(date2_str, "%Y-%m-%d")
        difference = abs(date1 - date2).days
        return difference
if __name__ == '__main__':
    calculator = DateCalculator()
    date1 = "2023-01-01"
    date2 = "2023-01-10"
    difference = calculator.get_difference(date1, date2)
    print(difference)