class NumberReverser:
    @staticmethod
    def reverse(a, b):
        return (b, a)

if __name__ == '__main__':
    reversed_numbers = NumberReverser.reverse(3, 5)
    print(reversed_numbers)