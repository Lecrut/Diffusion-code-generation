from collections import deque

class Queue:
    MAX_SIZE = 100

    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        if len(self.items) < self.MAX_SIZE:
            self.items.append(item)
        else:
            raise OverflowError('Queue is full')

    def dequeue(self):
        if not self.is_empty():
            return self.items.popleft()
        else:
            raise IndexError('Queue is empty')

    def is_empty(self):
        return len(self.items) == 0
if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.is_empty())
    for _ in range(98):
        queue.enqueue(_)
    try:
        queue.enqueue(100)
    except OverflowError as e:
        print(e)
    while not queue.is_empty():
        print(queue.dequeue())