def multiply_numbers(a, b):
    return a * b

class NumberMultiplier:
    def __init__(self):
        self.pi = 3.141592653589793
        self.e = 2.718281828459045
    
    def multiply_pi_by_e(self):
        return self.multiply(self.pi, self.e)
    
    def multiply(self, a, b):
        return a * b

if __name__ == '__main__':
    multiplier = NumberMultiplier()
    result_pi_e = multiplier.multiply_pi_by_e()
    print(result_pi_e)