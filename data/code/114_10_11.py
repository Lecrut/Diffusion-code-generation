class Multiplier:
    def multiply(self, a, b):
        return a * b

if __name__ == '__main__':
    multiplier = Multiplier()
    result1 = multiplier.multiply(5, 4)
    print(f"5 * 4 = {result1}")
    result2 = multiplier.multiply(10.5, 2)
    print(f"10.5 * 2 = {result2}")
    result3 = multiplier.multiply(-3, 7)
    print(f"-3 * 7 = {result3}")