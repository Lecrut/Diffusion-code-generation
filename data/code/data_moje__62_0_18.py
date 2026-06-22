def _find_divisors_pairs(n):
    divisors = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            divisors.append(i)
            if i * i != n:
                divisors.append(n // i)
        i += 1
    return divisors

def _sort_list(items):
    length = len(items)
    for i in range(length):
        for j in range(0, length - i - 1):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
    return items

def find_all_divisors(n):
    if n == 0:
        return []
    if n < 0:
        n = -n
    found = _find_divisors_pairs(n)
    return _sort_list(found)

class DivisorCalculator:
    def __init__(self, number):
        self.number = number
    
    def calculate(self):
        return find_all_divisors(self.number)

if __name__ == '__main__':
    test_value = 36
    solver = DivisorCalculator(test_value)
    result = solver.calculate()
    print(result)