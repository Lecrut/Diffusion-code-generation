class NumberReverser:
    def reverse_order(self, num1, num2):
        return [num2, num1]

if __name__ == '__main__':
    reverser = NumberReverser()
    result = reverser.reverse_order(30, 45)
    print(result)
    result2 = reverser.reverse_order(60, 75)
    print(result2)