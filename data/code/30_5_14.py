class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0

def decimal_to_binary(n):
    if n == 0:
        return "0"
    
    stack = Stack()
    num = n
    
    while num > 0:
        remainder = num % 2
        stack.push(remainder)
        num = num // 2
    
    binary_string = ""
    while not stack.is_empty():
        binary_string += str(stack.pop())
    
    return binary_string

if __name__ == '__main__':
    test_values = [0, 1, 2, 5, 10, 15, 16, 31, 64, 127, 255]
    for val in test_values:
        result = decimal_to_binary(val)
        print(f"{val} -> {result}")