class Adder:
    @staticmethod
    def add(a, b):
        return a + b

if __name__ == '__main__':
    result = Adder.add(5, 3)
    print(result)