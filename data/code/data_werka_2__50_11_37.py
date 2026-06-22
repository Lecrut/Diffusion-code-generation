class SymmetricDifferenceCalculator:

    def __init__(self, set1, set2):
        self.set1 = set1
        self.set2 = set2

    def calculate(self):
        return self.set1 ^ self.set2
if __name__ == '__main__':
    set_a = {1, 2, 3, 4}
    set_b = {3, 4, 5, 6}
    calculator_ab = SymmetricDifferenceCalculator(set_a, set_b)
    result_ab = calculator_ab.calculate()
    print('Symmetric difference of set_a and set_b:', result_ab)
    set_c = {'a', 'b', 'c'}
    set_d = {'b', 'c', 'd'}
    calculator_cd = SymmetricDifferenceCalculator(set_c, set_d)
    result_cd = calculator_cd.calculate()
    print('Symmetric difference of set_c and set_d:', result_cd)