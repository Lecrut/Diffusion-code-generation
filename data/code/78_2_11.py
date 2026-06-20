class MonthCalculator:
    def __init__(self):
        self.months = {
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

    def find_difference(self, month1_str, month2_str):
        month1_index = self.months.get(month1_str.lower(), -1)
        month2_index = self.months.get(month2_str.lower(), -1)

        if month1_index == -1 or month2_index == -1:
            raise ValueError("Invalid month name")

        return abs(month1_index - month2_index)

if __name__ == '__main__':
    calculator = MonthCalculator()
    print(calculator.find_difference("January", "March"))