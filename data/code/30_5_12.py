class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

def decimal_to_binary(n):
    if n == 0:
        return "0"
    stack = Stack()
    num = abs(n)
    while num > 0:
        remainder = num % 2
        stack.push(str(remainder))
        num = num // 2
    binary_string = ""
    while not stack.is_empty():
        binary_string += stack.pop()
    if n < 0:
        binary_string = "-" + binary_string
    return binary_string

if __name__ == '__main__':
    sample_values = [0, 1, 2, 5, 10, 15, 32, 100, -5]
    for value in sample_values:
        result = decimal_to_binary(value)
        print(f"{value} -> {result}")