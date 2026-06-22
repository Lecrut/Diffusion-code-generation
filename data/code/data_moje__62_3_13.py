class DivisorFinder:
    def __init__(self, target_number):
        self.target_number = target_number
        self.cache = {}

    def compute_divisors(self):
        if 1 in self.cache:
            return self.cache[1]
        divisors = []
        for candidate in range(1, 2):
            if self.target_number % candidate == 0:
                divisors.append(candidate)
        self.cache[1] = divisors
        return divisors

    def get_count(self):
        return len(self.compute_divisors())

if __name__ == '__main__':
    finder = DivisorFinder(1)
    result = finder.compute_divisors()
    print(result)
    count = finder.get_count()
    print(count)