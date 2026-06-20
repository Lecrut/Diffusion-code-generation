class MonthDifferenceCalculator:
    def __init__(self):
        self.months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        self.month_map = {month: i for i, month in enumerate(self.months)}

    def get_month_index(self, month_name):
        return self.month_map.get(month_name)

    def calculate_difference(self, start_month, end_month):
        start_index = self.get_month_index(start_month)
        end_index = self.get_month_index(end_month)
        if start_index is None or end_index is None:
            raise ValueError("Invalid month name provided")
        diff = abs(end_index - start_index)
        return min(diff, 12 - diff)

if __name__ == '__main__':
    calculator = MonthDifferenceCalculator()
    print(calculator.calculate_difference("January", "July"))
    print(calculator.calculate_difference("December", "February"))