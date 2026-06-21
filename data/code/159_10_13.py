class OddNumberFinder:
    START = 1
    END = 50

    @staticmethod
    def find_odd_numbers(start, end):
        return [num for num in range(start, end + 1) if num % 2 != 0]

if __name__ == '__main__':
    odd_finder = OddNumberFinder()
    result = odd_finder.find_odd_numbers(OddNumberFinder.START, OddNumberFinder.END)
    print(result)