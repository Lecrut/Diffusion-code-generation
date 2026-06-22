class IntegerAdder:
    @staticmethod
    def add(a, b):
        return a + b

if __name__ == '__main__':
    result = IntegerAdder.add(4, 6)
    print(result)