from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.popleft()
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

if __name__ == '__main__':
    queue = Queue()
    actions = ['enqueue(1)', 'enqueue(2)', 'dequeue()', 'enqueue(3)', 'size()', 'dequeue()', 'dequeue()']
    
    for action in actions:
        if action.startswith('enqueue'):
            _, value = action.split('(')
            value = int(value[:-1])
            queue.enqueue(value)
        elif action == 'dequeue':
            print(queue.dequeue())
        elif action == 'size':
            print(queue.size())