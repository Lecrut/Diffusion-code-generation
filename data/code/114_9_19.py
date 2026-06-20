class Multiplier:
    def multiply(self, x, y):
        return x * y

if __name__ == '__main__':
    multiplier = Multiplier()
    result1 = multiplier.multiply(7, 8)
    print(result1)
    result2 = multiplier.multiply(3.5, 4)
    print(result2)