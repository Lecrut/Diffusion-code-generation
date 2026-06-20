class MonthCalculator:
    def __init__(self):
        self.months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    
    def get_month_index(self, month_name):
        return self.months.index(month_name)
    
    def month_difference(self, start_month, end_month):
        start_index = self.get_month_index(start_month)
        end_index = self.get_month_index(end_month)
        diff = abs(end_index - start_index)
        return min(diff, 12 - diff)

if __name__ == '__main__':
    calculator = MonthCalculator()
    result = calculator.month_difference("January", "July")
    print(result)