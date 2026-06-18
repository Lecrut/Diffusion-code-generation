class QuantityAdder:
    def add(self, quantity1, quantity2):
        return quantity1 + quantity2
if __name__ == '__main__':
    adder = QuantityAdder()
    a = 10
    b = 5
    result = adder.add(a, b)
    print(result)