class QuantityAdder:
    def add(self, quantity1, quantity2):
        return quantity1 + quantity2
if __name__ == '__main__':
    adder = QuantityAdder()
    result = adder.add(10, 5)
    print(result)