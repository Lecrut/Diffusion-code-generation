class Multiplier:
    def multiply(self, a: float, b: float) -> float:
        return a * b

if __name__ == '__main__':
    multiplier_instance = Multiplier()
    result1 = multiplier_instance.multiply(3.5, 2.0)
    result2 = multiplier_instance.multiply(-4.0, -2.5)
    print(result1, result2)