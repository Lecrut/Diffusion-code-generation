class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

def decimal_to_binary_stack(n):
    if n == 0:
        return "0"
    if n < 0:
        sign = "-"
        n = -n
    else:
        sign = ""
    stack = Stack()
    while n > 0:
        remainder = n % 2
        stack.push(remainder)
        n = n // 2
    binary_string = ""
    while not stack.is_empty():
        binary_string += str(stack.pop())
    return sign + binary_string

if __name__ == '__main__':
    sample_numbers = [0, 1, 2, 5, 10, 15, 255, 1024]
    for number in sample_numbers:
        result = decimal_to_binary_stack(number)
        print(f"{number}: {result}")
    negative_test = decimal_to_binary_stack(-10)
    print(f"-10: {negative_test}")