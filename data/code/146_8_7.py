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
    actions = [
        ('enqueue', 'a'),
        ('enqueue', 'b'),
        ('dequeue',),
        ('enqueue', 'c'),
        ('dequeue',),
        ('dequeue',),
        ('is_empty',)
    ]

    for action, *args in actions:
        if action == 'enqueue':
            q.enqueue(args[0])
        elif action == 'dequeue':
            print(q.dequeue())
        elif action == 'is_empty':
            print(q.is_empty())