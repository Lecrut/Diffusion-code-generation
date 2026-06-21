from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.popleft() if self.items else None

if __name__ == '__main__':
    q = Queue()
    actions = [('enqueue', 1), ('enqueue', 2), ('dequeue',), ('enqueue', 3), ('dequeue',), ('dequeue',)]
    for action in actions:
        method, *args = action
        if method == 'enqueue':
            q.enqueue(*args)
        elif method == 'dequeue':
            print(q.dequeue())