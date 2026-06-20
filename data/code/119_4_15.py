class NumberReverser:
    @staticmethod
    def reverse(a, b):
        return (b, a)

if __name__ == '__main__':
    result = NumberReverser.reverse(3, 5)
    print(result)