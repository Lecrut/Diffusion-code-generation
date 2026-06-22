class DivisorFinder:
    def __init__(self, number):
        self.number = number

    def find(self):
        if self.number <= 0:
            return []
        divisors = []
        i = 1
        while i * i <= self.number:
            if self.number % i == 0:
                divisors.append(i)
                second_divisor = self.number // i
                if second_divisor != i:
                    divisors.append(second_divisor)
            i += 1
        return sorted(divisors)

def get_divisors_of_60():
    finder = DivisorFinder(60)
    return finder.find()

if __name__ == '__main__':
    print(get_divisors_of_60())