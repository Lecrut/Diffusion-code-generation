class MonthCalculator:
    MONTHS = {
        "january": 0,
        "february": 1,
        "march": 2,
        "april": 3,
        "may": 4,
        "june": 5,
        "july": 6,
        "august": 7,
        "september": 8,
        "october": 9,
        "november": 10,
        "december": 11
    }

    @staticmethod
    def normalize_month_name(month_str):
        return month_str.lower()

    def find_difference(self, month1_str, month2_str):
        normalized_month1 = self.normalize_month_name(month1_str)
        normalized_month2 = self.normalize_month_name(month2_str)
        return abs(self.MONTHS[normalized_month1] - self.MONTHS[normalized_month2])

if __name__ == '__main__':
    calculator = MonthCalculator()
    print(calculator.find_difference("January", "March"))