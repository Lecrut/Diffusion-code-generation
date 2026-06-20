class NumberOperations:
    PI = 3.141592653589793
    E = 2.718281828459045

    @staticmethod
    def multiply(a, b):
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise ValueError("Both inputs must be numbers")
        return a * b

if __name__ == '__main__':
    multiplier = NumberOperations()
    result = multiplier.multiply(NumberOperations.PI, NumberOperations.E)
    print(result)