from typing import Any

class NumberReverser:
    def reverse_order(self, num1: int, num2: int) -> tuple:
        return (num2, num1)

if __name__ == '__main__':
    reverser = NumberReverser()
    num_a = 3
    num_b = 8
    result = reverser.reverse_order(num_a, num_b)
    print(result)