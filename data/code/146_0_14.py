class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

if __name__ == '__main__':
    sample_elements = [3, 7, 2, 5, 9]
    stack = Stack()

    for element in sample_elements:
        stack.push(element)

    print(f"Stack after pushing elements: {stack.items}")

    while not stack.is_empty():
        popped_element = stack.pop()
        print(f"Popped element: {popped_element}")