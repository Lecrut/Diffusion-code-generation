class BitwiseSwapper:
    def swap(self, a, b):
        a = a ^ b
        b = a ^ b
        a = a ^ b
        return a, b

if __name__ == '__main__':
    swapper = BitwiseSwapper()
    x, y = 10, 20
    swapped_values = swapper.swap(x, y)
    print(swapped_values)