class NumberReverser:
    @staticmethod
    def reverse_numbers(a, b):
        return (b, a)

if __name__ == '__main__':
    reverser = NumberReverser()
    result = reverser.reverse_numbers(3, 5)
    print(result)