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
    actions = ['enqueue(1)', 'enqueue(2)', 'dequeue()', 'enqueue(3)', 'dequeue()', 'dequeue()']
    results = []
    for action in actions:
        cmd, *args = action.split('(')
        args = [arg.strip(')').strip("'") for arg in args]
        if cmd == 'enqueue':
            q.enqueue(int(args[0]))
        elif cmd == 'dequeue':
            result = q.dequeue()
            results.append(result)
    print(results)