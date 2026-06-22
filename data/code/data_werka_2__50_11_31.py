class SymmetricDifferenceCalculator:

    def __init__(self):
        self.set1 = None
        self.set2 = None

    def set_sets(self, set1, set2):
        if not isinstance(set1, set) or not isinstance(set2, set):
            raise ValueError('Both arguments must be sets.')
        self.set1 = set1
        self.set2 = set2

    def calculate_symmetric_difference(self):
        return self.set1 ^ self.set2
if __name__ == '__main__':
    calculator = SymmetricDifferenceCalculator()
    set_a = {1, 2, 3, 4}
    set_b = {3, 4, 5, 6}
    calculator.set_sets(set_a, set_b)
    result_ab = calculator.calculate_symmetric_difference()
    print('Symmetric difference of set_a and set_b:', result_ab)
    set_c = {'a', 'b', 'c'}
    set_d = {'b', 'c', 'd'}
    calculator.set_sets(set_c, set_d)
    result_cd = calculator.calculate_symmetric_difference()
    print('Symmetric difference of set_c and set_d:', result_cd)