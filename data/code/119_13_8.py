class NumberSwapper:
    @staticmethod
    def swap(a, b):
        return b, a

if __name__ == '__main__':
    x, y = 15, 25
    swapped_x, swapped_y = NumberSwapper.swap(x, y)
    print(f"Before swap: x={x}, y={y}")
    print(f"After swap: x={swapped_x}, y={swapped_y}")