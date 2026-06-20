class DateCalculator:
    def get_next_month_date(self, year, month):
        if not isinstance(year, int) or not isinstance(month, int):
            raise ValueError("Year and month must be integers.")
        if year < 1 or month < 1 or month > 12:
            raise ValueError("Invalid date values provided.")
        
        if month == 12:
            next_month = 1
            next_year = year + 1
        else:
            next_month = month + 1
            next_year = year
        
        return next_year, next_month

if __name__ == '__main__':
    calculator = DateCalculator()
    current_year = 2023
    current_month = 10
    try:
        next_year, next_month = calculator.get_next_month_date(current_year, current_month)
        print(f"The date of the next month for {current_year}-{current_month:02d} is {next_year}-{next_month:02d}")
    except ValueError as e:
        print(e)

    current_year = 2024
    current_month = 12
    try:
        next_year, next_month = calculator.get_next_month_date(current_year, current_month)
        print(f"The date of the next month for {current_year}-{current_month:02d} is {next_year}-{next_month:02d}")
    except ValueError as e:
        print(e)