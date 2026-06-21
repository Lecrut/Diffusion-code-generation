from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.popleft() if self.items else None

    def is_empty(self):
        return len(self.items) == 0

if __name__ == '__main__':
    q = Queue()
    actions = [('enqueue', 1), ('enqueue', 2), ('dequeue',), ('enqueue', 3), ('dequeue',), ('dequeue',)]
    for action in actions:
        if action[0] == 'enqueue':
            q.enqueue(action[1])
        elif action[0] == 'dequeue':
            print(q.dequeue())