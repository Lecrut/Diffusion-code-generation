class SwapValues:
    @staticmethod
    def swap(a, b):
        values = [a, b]
        values[0], values[1] = values[1], values[0]
        return values

if __name__ == '__main__':
    x, y = 5, 10
    swapped_values = SwapValues.swap(x, y)
    print(f"Swapped values: x={swapped_values[0]}, y={swapped_values[1]}")