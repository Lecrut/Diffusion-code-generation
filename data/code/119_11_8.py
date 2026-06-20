class NumberReverser:
    def reverse_numbers(self, a, b):
        a = a - b
        b = a + 2 * b
        a = b - a
        return a, b

if __name__ == '__main__':
    reverser = NumberReverser()
    num1 = 15
    num2 = 30
    result = reverser.reverse_numbers(num1, num2)
    print(result)