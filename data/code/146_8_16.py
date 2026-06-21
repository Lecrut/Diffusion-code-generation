from collections import deque

def main():
    queue = deque()
    queue.append('a')
    queue.append('b')
    queue.append('c')
    print(queue.popleft())
    print(queue.popleft())
    print(queue)
if __name__ == '__main__':
    main()