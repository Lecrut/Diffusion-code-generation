class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop() if not self.is_empty() else None

    def peek(self):
        return self.items[-1] if not self.is_empty() else None

    def is_empty(self):
        return len(self.items) == 0
if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    print(stack.pop())
    stack.push('a')
    print(stack.peek())
    print(stack.is_empty())
    print(stack.pop())
    print(stack.is_empty())