class NumberReverser:
    def reverse_order(self, num1, num2):
        numbers = [num1, num2]
        numbers.sort(reverse=True)
        return numbers
if __name__ == '__main__':
    reverser = NumberReverser()
    num_a = 10
    num_b = 5
    result = reverser.reverse_order(num_a, num_b)
    print(result)