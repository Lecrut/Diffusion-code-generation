class NumberSwapper:
    @staticmethod
    def swap(a, b):
        a = a ^ b
        b = a ^ b
        a = a ^ b
        return a, b

if __name__ == '__main__':
    x, y = 15, 25
    print(NumberSwapper.swap(x, y))