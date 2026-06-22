class PreciseAdder:
    @staticmethod
    def add(a: float, b: float) -> float:
        return a + b

if __name__ == '__main__':
    result = PreciseAdder.add(0.1, 0.2)
    print(result)