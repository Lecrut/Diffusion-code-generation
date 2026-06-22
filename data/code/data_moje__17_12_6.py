from collections import deque

class DequeStructure:
    def __init__(self):
        self.deque = deque()

    def add_item(self, item):
        self.deque.append(item)

    def pop_last_added(self):
        return self.deque.pop()

def create_and_pop():
    d = DequeStructure()
    d.add_item(10)
    d.add_item(20)
    d.add_item(30)
    d.add_item(40)
    d.add_item(50)
    return d.pop_last_added()

if __name__ == '__main__':
    result = create_and_pop()
    print(result)