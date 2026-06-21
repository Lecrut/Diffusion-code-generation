class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

def decimal_to_binary(n):
    if n == 0:
        return "0"
    stack = Stack()
    while n > 0:
        remainder = n % 2
        stack.push(str(remainder))
        n = n // 2
    binary_string = ""
    while not stack.is_empty():
        binary_string += stack.pop()
    return binary_string

if __name__ == '__main__':
    sample_values = [0, 1, 2, 5, 10, 42, 255, 1024]
    for value in sample_values:
        result = decimal_to_binary(value)
        print(f"{value} -> {result}")