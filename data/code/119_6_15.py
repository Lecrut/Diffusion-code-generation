class NumberReverser:
    @staticmethod
    def reverse_numbers(a, b):
        while a != 0:
            temp = a
            a = b - (b // a) * a
            b = temp
        return b

if __name__ == '__main__':
    reverser = NumberReverser()
    result = reverser.reverse_numbers(123456789, 987654321)
    print(result)