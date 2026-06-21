from collections import deque

def queue_operations():
    queue = deque()
    queue.append('A')
    queue.append('B')
    queue.append('C')
    print(queue.popleft())
    print(queue.popleft())
    print(queue)
if __name__ == '__main__':
    queue_operations()