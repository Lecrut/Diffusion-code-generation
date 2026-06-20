class NumberReverser:
    @staticmethod
    def reverse_order(num1, num2):
        return [num2, num1]

if __name__ == '__main__':
    reverser = NumberReverser()
    result = reverser.reverse_order(10, 20)
    print(result)