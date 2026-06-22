class DivisorFinder:
    def __init__(self, number):
        self.number = number

    def compute_divisors(self):
        divisors = []
        limit = int(self.number**0.5)
        for i in range(1, limit + 1):
            if self.number % i == 0:
                divisors.append(i)
                other = self.number // i
                if i != other:
                    divisors.append(other)
        divisors.sort()
        return divisors

    def is_perfect(self):
        divs = self.compute_divisors()
        divs.remove(self.number)
        return sum(divs) == self.number

    def count_divisors(self):
        return len(self.compute_divisors())

if __name__ == '__main__':
    finder = DivisorFinder(100)
    print(finder.compute_divisors())
    print(finder.count_divisors())
    print(finder.is_perfect())