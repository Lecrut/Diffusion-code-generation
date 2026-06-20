class YearDifference:
    MIN_YEAR = 1900
    MAX_YEAR = 2100

    @staticmethod
    def calculate_difference(year1, year2):
        if not (YearDifference.MIN_YEAR <= year1 <= YearDifference.MAX_YEAR and 
                YearDifference.MIN_YEAR <= year2 <= YearDifference.MAX_YEAR):
            raise ValueError("Both years must be between 1900 and 2100.")
        return abs(year1 - year2)

if __name__ == '__main__':
    result = YearDifference.calculate_difference(2023, 1985)
    print(result)