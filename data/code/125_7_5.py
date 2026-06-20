class BasicMath:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

if __name__ == '__main__':
    print(BasicMath.add(5, 3))
    print(BasicMath.subtract(10, 4))