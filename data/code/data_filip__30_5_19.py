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
    
    if n < 0:
        return "-" + decimal_to_binary(-n)
    
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

if __name__ == "__main__":
    print(decimal_to_binary(10))
    print(decimal_to_binary(255))
    print(decimal_to_binary(0))
    print(decimal_to_binary(-15))