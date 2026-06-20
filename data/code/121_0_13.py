class MagnitudeComparator:
    @staticmethod
    def compare(a, b):
        if a > b:
            return a
        elif b > a:
            return b
        else:
            return None

if __name__ == '__main__':
    value1 = 123456789012345678901234567890
    value2 = 987654321098765432109876543210
    larger_value = MagnitudeComparator.compare(value1, value2)
    print(f"Value A: {value1}")
    print(f"Value B: {value2}")
    if larger_value is not None:
        print(f"The larger value is: {larger_value}")
    else:
        print("The values are the same")