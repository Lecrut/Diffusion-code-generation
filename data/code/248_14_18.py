class NumberAdder:
    @staticmethod
    def add(a, b):
        return a + b

if __name__ == '__main__':
    result = NumberAdder.add(3, 5)
    print(result)