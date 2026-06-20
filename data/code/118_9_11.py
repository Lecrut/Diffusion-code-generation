class Multiplier:
    def multiply(self, a, b):
        return math.prod([a, b])

if __name__ == '__main__':
    multiplier = Multiplier()
    result1 = multiplier.multiply(15, 7)
    print(result1)
    result2 = multiplier.multiply(12, 5)
    print(result2)