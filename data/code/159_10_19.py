class OddNumberFinder:
    def find_odds(self, start, end):
        return [num for num in range(start, end + 1) if num % 2 != 0]

if __name__ == '__main__':
    finder = OddNumberFinder()
    sample_start = 1
    sample_end = 50
    result = finder.find_odds(sample_start, sample_end)
    print(result)