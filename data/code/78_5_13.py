class MonthDistanceCalculator:
    MONTHS = ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"]
    
    @staticmethod
    def month_index(month_name):
        return MonthDistanceCalculator.MONTHS.index(month_name)
    
    @classmethod
    def calculate_difference(cls, start_month, end_month):
        start_idx = cls.month_index(start_month)
        end_idx = cls.month_index(end_month)
        diff = abs(end_idx - start_idx)
        return min(diff, 12 - diff)

if __name__ == '__main__':
    calc = MonthDistanceCalculator()
    result = calc.calculate_difference("January", "July")
    print(result)