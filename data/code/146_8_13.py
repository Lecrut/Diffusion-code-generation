from collections import deque

def queue_operations():
    q = deque()
    q.append('A')
    q.append('B')
    q.append('C')
    print(q.popleft())
    print(q.popleft())
    print(len(q) == 0)
    q.append('D')
    print(q[0])
if __name__ == '__main__':
    queue_operations()