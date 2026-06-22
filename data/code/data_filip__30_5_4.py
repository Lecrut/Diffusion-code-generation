class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def is_empty(self):
        return len(self._items) == 0

def decimal_to_binary(n):
    if n == 0:
        return "0"
    stack = Stack()
    num = n if n > 0 else -n
    while num > 0:
        stack.push(str(num % 2))
        num //= 2
    binary_digits = []
    while not stack.is_empty():
        binary_digits.append(stack.pop())
    binary_string = "".join(binary_digits)
    return binary_string if n >= 0 else "-" + binary_string

if __name__ == "__main__":
    test_values = [0, 1, 10, 255, 42, -7]
    for val in test_values:
        print(f"{val} -> {decimal_to_binary(val)}")