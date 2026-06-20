class YearCalculator:
    def find_absolute_difference(self, year1, year2):
        if not isinstance(year1, int) or not isinstance(year2, int):
            raise ValueError("Both inputs must be integers.")
        
        return abs(year1 - year2)

if __name__ == '__main__':
    calculator = YearCalculator()
    years1 = 2023
    years2 = 1998
    difference = calculator.find_absolute_difference(years1, years2)
    print(f"The absolute difference between {years1} and {years2} is {difference}")