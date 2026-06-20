import datetime

class DateCalculator:
    def validate_date_format(self, date_str):
        try:
            datetime.datetime.strptime(date_str, "%Y-%m-%d")
            return True
        except ValueError:
            return False

    def calculate_difference(self, date1_str, date2_str):
        if not self.validate_date_format(date1_str) or not self.validate_date_format(date2_str):
            raise ValueError("Dates must be in 'YYYY-MM-DD' format")

        date1 = datetime.datetime.strptime(date1_str, "%Y-%m-%d")
        date2 = datetime.datetime.strptime(date2_str, "%Y-%m-%d")
        difference = abs(date2 - date1)
        return difference

if __name__ == '__main__':
    calculator = DateCalculator()
    difference = calculator.calculate_difference('2023-01-01', '2023-01-15')
    print(difference)