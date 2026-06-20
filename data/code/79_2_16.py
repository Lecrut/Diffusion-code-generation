class DateCalculator:
    def get_next_month_date(self, year, month):
        months = {
            1: (year + 1, 1),
            2: (year, month + 1),
            3: (year, month + 1),
            4: (year, month + 1),
            5: (year, month + 1),
            6: (year, month + 1),
            7: (year, month + 1),
            8: (year, month + 1),
            9: (year, month + 1),
            10: (year, month + 1),
            11: (year, month + 1),
            12: (year + 1, 1)
        }
        return months[month]

if __name__ == '__main__':
    calculator = DateCalculator()
    current_year = 2023
    current_month = 10
    next_year, next_month = calculator.get_next_month_date(current_year, current_month)
    print(f"The date of the next month for {current_year}-{current_month:02d} is {next_year}-{next_month:02d}")
    current_year = 2024
    current_month = 12
    next_year, next_month = calculator.get_next_month_date(current_year, current_month)
    print(f"The date of the next month for {current_year}-{current_month:02d} is {next_year}-{next_month:02d}")