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
    sample_elements = [1, 2, 3, 4, 5]
    stack = Stack()
    for element in sample_elements:
        stack.push(element)
    print('Popped:', stack.pop())
    print('Peeked:', stack.peek())
    print('Is empty?', stack.is_empty())