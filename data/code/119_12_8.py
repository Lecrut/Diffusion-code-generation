class NumberReverser:
    def reverse_order(self, num1, num2):
        return [num2 ^ (num1 & ~num2), num1 ^ (~num1 & num2)]

if __name__ == '__main__':
    reverser = NumberReverser()
    result = reverser.reverse_order(10, 20)
    print(result)
    result2 = reverser.reverse_order(5, 15)
    print(result2)