class NumberMultiplier:
    def __init__(self):
        self.pi = 3.141592653589793
        self.e = 2.718281828459045

    def multiply(self, a, b):
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise ValueError("Both inputs must be numbers")
        return a * b

if __name__ == '__main__':
    multiplier = NumberMultiplier()
    result1 = multiplier.multiply(3.141592653589793, 2.718281828459045)
    result2 = multiplier.multiply(multiplier.pi, multiplier.e)
    print(result1)
    print(result2)