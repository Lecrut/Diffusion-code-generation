class QuantityAdder:
    def add(self, a, b):
        return a + b
if __name__ == '__main__':
    adder = QuantityAdder()
    result1 = adder.add(10, 5)
    print(f"10 + 5 = {result1}")
    result2 = adder.add(100, -30)
    print(f"100 + (-30) = {result2}")