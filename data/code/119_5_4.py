class ValueSwapper:
    @staticmethod
    def swap(a, b):
        values = [a, b]
        values[0], values[1] = values[1], values[0]
        return values

if __name__ == '__main__':
    num1 = 15
    num2 = 25
    swapped_values = ValueSwapper.swap(num1, num2)
    print(swapped_values)