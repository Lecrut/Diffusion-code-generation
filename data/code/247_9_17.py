class Adder:
    @staticmethod
    def add(a, b):
        return int(a) + int(b)

if __name__ == '__main__':
    result = Adder.add(10, 5)
    print(result)