class BitwiseXorSwapper:
    @staticmethod
    def swap(a, b):
        a = a ^ b
        b = a ^ b
        a = a ^ b
        return a, b

if __name__ == '__main__':
    x, y = 100, 200
    print(BitwiseXorSwapper.swap(x, y))