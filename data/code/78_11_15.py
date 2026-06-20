class MonthCalculator:
    @staticmethod
    def months_elapsed(start_month, end_month):
        return abs(end_month - start_month)

if __name__ == '__main__':
    calc = MonthCalculator()
    result1 = calc.months_elapsed(1, 5)
    print(f"Start: 1, End: 5, Elapsed: {result1}")
    result2 = calc.months_elapsed(10, 3)
    print(f"Start: 10, End: 3, Elapsed: {result2}")
    result3 = calc.months_elapsed(12, 12)
    print(f"Start: 12, End: 12, Elapsed: {result3}")