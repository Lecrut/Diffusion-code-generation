class NumericOperations:
    @classmethod
    def multiply(cls, a, b):
        if not (isinstance(a, int) and isinstance(b, int)):
            raise ValueError("Both inputs must be integers")
        result = 0
        negative_result = False

        if a < 0:
            a = -a
            negative_result = not negative_result
        if b < 0:
            b = -b
            negative_result = not negative_result

        while b > 0:
            if b & 1:
                result += a
            a <<= 1
            b >>= 1

        return -result if negative_result else result

if __name__ == '__main__':
    sample_product = NumericOperations.multiply(5, -3)
    print(sample_product)