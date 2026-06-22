class SumCalculator:
    @staticmethod
    def sum_five_integers(a, b, c, d, e):
        total = 0
        numbers = [a, b, c, d, e]
        for number in numbers:
            total += number
        return total

if __name__ == '__main__':
    result = SumCalculator.sum_five_integers(10, 25, 30, 5, 15)
    print(result)