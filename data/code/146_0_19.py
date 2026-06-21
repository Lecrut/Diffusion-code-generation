class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        if not isinstance(item, (int, str)):
            raise ValueError('Invalid input. Only integers and strings are allowed.')
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0
if __name__ == '__main__':
    stack = Stack()
    stack.push(5)
    stack.push('hello')
    print(stack.pop())
    print(stack.peek())
    print(stack.is_empty())
    print(stack.pop())
    print(stack.is_empty())