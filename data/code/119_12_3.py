class NumberReverser:
    def reverse_order(self, num1, num2):
        return [num2, num1]
if __name__ == '__main__':
    reverser = NumberReverser()
    num_a = 10
    num_b = 25
    result = reverser.reverse_order(num_a, num_b)
    print(result)