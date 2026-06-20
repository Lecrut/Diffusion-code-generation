class MathOperations:
    @classmethod
    def multiply(cls, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError("Both inputs must be numbers")
        
        return int(a * b)

if __name__ == '__main__':
    result = MathOperations.multiply(4, 3)
    print(result)