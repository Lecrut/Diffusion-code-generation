class NumberReverser:
    @staticmethod
    def reverse_order(num1: int, num2: int) -> tuple:
        return (num2, num1)

if __name__ == '__main__':
    reverser = NumberReverser()
    num_a = 10
    num_b = 5
    result = reverser.reverse_order(num_a, num_b)
    print(result)