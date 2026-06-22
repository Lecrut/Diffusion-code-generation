class RatioFinder:
    def __init__(self, target_ratio):
        self.target_ratio = target_ratio

    def find_pairs(self, numbers):
        pairs = []
        seen = set()
        for num in numbers:
            if num == 0:
                continue
            complement = num * self.target_ratio
            if complement in seen:
                pairs.append((int(complement), num))
            seen.add(num)
        return pairs

if __name__ == '__main__':
    finder = RatioFinder(2)
    sample_numbers = [1, 2, 3, 4, 5, 6, 8, 10]
    pairs = finder.find_pairs(sample_numbers)
    for pair in pairs:
        print(pair)