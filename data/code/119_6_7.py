class NumberReverser:
    MAX_ITERATIONS = 1000

    @staticmethod
    def reverse_numbers(a, b):
        for _ in range(NumberReverser.MAX_ITERATIONS):
            if a == 0:
                break
            temp = a
            a = b - (b // a) * a
            b = temp
        return b

if __name__ == '__main__':
    x = 123456789
    y = 987654321
    result = NumberReverser.reverse_numbers(x, y)
    print(f"x: {x}, y: {y} -> Reversed value: {result}")