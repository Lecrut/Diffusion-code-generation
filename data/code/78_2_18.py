class MonthCalculator:
    def find_difference(self, month1_str, month2_str):
        months = ["january", "february", "march", "april", "may", "june",
                  "july", "august", "september", "october", "november", "december"]
        index1 = months.index(month1_str.lower())
        index2 = months.index(month2_str.lower())
        return abs(index1 - index2)

if __name__ == '__main__':
    calculator = MonthCalculator()
    print(calculator.find_difference("January", "March"))