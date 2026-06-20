class MonthDifferenceCalculator:
    MONTHS = {
        "january": 1, "february": 2, "march": 3, "april": 4,
        "may": 5, "june": 6, "july": 7, "august": 8,
        "september": 9, "october": 10, "november": 11, "december": 12
    }

    @staticmethod
    def calculate_difference(month1_name, month2_name):
        if month1_name not in MonthDifferenceCalculator.MONTHS or month2_name not in MonthDifferenceCalculator.MONTHS:
            raise ValueError("Invalid month name provided.")
        month1 = MonthDifferenceCalculator.MONTHS[month1_name]
        month2 = MonthDifferenceCalculator.MONTHS[month2_name]
        difference = abs(month1 - month2)
        return difference

if __name__ == '__main__':
    calculator = MonthDifferenceCalculator()
    month_a = "December"
    month_b = "March"
    try:
        diff = calculator.calculate_difference(month_a.lower(), month_b.lower())
        print(diff)
    except ValueError as e:
        print(e)