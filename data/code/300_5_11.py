import calendar

class DaysLeftInMonth:
    def __init__(self):
        self.current_date = datetime.date.today()
    
    def days_left(self):
        _, num_days_in_month = calendar.monthrange(self.current_date.year, self.current_date.month)
        return num_days_in_month - self.current_date.day

if __name__ == '__main__':
    days_calculator = DaysLeftInMonth()
    result = days_calculator.days_left()
    print(result)