import datetime

class DateDifferenceCalculator:
    @staticmethod
    def parse_date(date_str):
        formats = ['%m/%d/%Y', '%Y-%m-%d']
        for fmt in formats:
            try:
                return datetime.datetime.strptime(date_str, fmt)
            except ValueError:
                continue
        raise ValueError("Invalid date format. Please use MM/DD/YYYY or YYYY-MM-DD.")

    def calculate_difference(self, date1_str, date2_str):
        date1 = self.parse_date(date1_str)
        date2 = self.parse_date(date2_str)
        difference = abs((date2 - date1).days)
        return difference

if __name__ == '__main__':
    calculator = DateDifferenceCalculator()
    result = calculator.calculate_difference("01/15/2023", "03/20/2024")
    print(result)