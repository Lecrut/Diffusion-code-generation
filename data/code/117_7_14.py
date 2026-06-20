class NumberSubtractor:
    def subtract(self, a, b):
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return float(a - b)
        else:
            raise ValueError('Both inputs must be numbers')

if __name__ == '__main__':
    subtrator = NumberSubtractor()
    result1 = subtrator.subtract(10, 5)
    result2 = subtrator.subtract(3.5, 1.2)
    print(result1)
    print(result2)