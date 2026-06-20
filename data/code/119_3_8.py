class BitwiseSwapper:
    @staticmethod
    def swap(a, b):
        a = a ^ b
        b = a ^ b
        a = a ^ b
        return a, b

if __name__ == '__main__':
    swapper = BitwiseSwapper()
    x, y = 10, 20
    print(swapper.swap(x, y))