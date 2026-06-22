class DivisorFinder:
    def __init__(self, number):
        if not isinstance(number, int):
            raise TypeError('Input must be an integer')
        if number <= 0:
            raise ValueError('Number must be a positive integer')
        self.number = number

    def find(self):
        divisors = []
        limit = int(self.number ** 0.5)
        for i in range(1, limit + 1):
            if self.number % i == 0:
                divisors.append(i)
                complement = self.number // i
                if i != complement:
                    divisors.append(complement)
        return sorted(divisors)

if __name__ == '__main__':
    sample_value = 360
    finder = DivisorFinder(sample_value)
    result = finder.find()
    print(result)