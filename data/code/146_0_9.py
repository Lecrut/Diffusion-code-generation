MAX_STACK_SIZE = 100

class Stack:
    def __init__(self):
        self.items = []
        self.top = -1

    def push(self, item):
        if self.is_full():
            raise IndexError("Stack overflow")
        self.top += 1
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        item = self.items.pop()
        self.top -= 1
        return item

    def peek(self):
        if self.is_empty():
            return None
        return self.items[self.top]

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return len(self.items) >= MAX_STACK_SIZE

if __name__ == '__main__':
    stack = Stack()
    sample_values = [1, 2, 3, 4, 5]
    for value in sample_values:
        stack.push(value)
    print("Stack after pushing:", stack.items)
    while not stack.is_empty():
        print(stack.pop())