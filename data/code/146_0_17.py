class Stack:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        if not isinstance(item, (int, str)):
            raise ValueError('Item must be an integer or a string')
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError('pop from empty stack')
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError('peek from empty stack')
        return self.items[-1]
if __name__ == '__main__':
    stack = Stack()
    stack.push(5)
    stack.push('a')
    print(stack.peek())
    print(stack.pop())
    print(stack.is_empty())
    print(stack.pop())
    try:
        print(stack.pop())
    except IndexError as e:
        print(e)