class MonthCalculator:
    def find_difference(self, month1_str, month2_str):
        months = ["january", "february", "march", "april", "may", "june",
                  "july", "august", "september", "october", "november", "december"]
        month1_index = months.index(month1_str.lower())
        month2_index = months.index(month2_str.lower())
        return abs(month1_index - month2_index)

if __name__ == '__main__':
    calculator = MonthCalculator()
    print(calculator.find_difference("January", "March"))