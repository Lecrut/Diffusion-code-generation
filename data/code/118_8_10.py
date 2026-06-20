class NumericOperations:
    @classmethod
    def multiply(cls, a, b):
        if not (isinstance(a, int) and isinstance(b, int)):
            raise ValueError("Both inputs must be integers.")
        
        return a * b

if __name__ == '__main__':
    result = NumericOperations.multiply(5, 6)
    print(result)