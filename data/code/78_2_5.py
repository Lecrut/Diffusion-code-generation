class MonthCalculator:
    MONTHS = ["january", "february", "march", "april", "may", "june",
              "july", "august", "september", "october", "november", "december"]

    def validate_month(self, month_str):
        if not isinstance(month_str, str) or len(month_str) == 0:
            raise ValueError("Month must be a non-empty string")
        return month_str.lower()

    def find_difference(self, month1_str, month2_str):
        month1_str = self.validate_month(month1_str)
        month2_str = self.validate_month(month2_str)

        month1_index = self.MONTHS.index(month1_str)
        month2_index = self.MONTHS.index(month2_str)

        return abs(month1_index - month2_index)

if __name__ == '__main__':
    calculator = MonthCalculator()
    print(calculator.find_difference("January", "March"))