from collections import deque

def perform_queue_operations():
    queue = deque()
    queue.append('A')
    queue.append('B')
    queue.append('C')
    print('Queue after enqueues:', list(queue))
    dequeued_item = queue.popleft()
    print(f'Dequeued item: {dequeued_item}')
    peeked_item = queue[0]
    print(f'Front item in the queue: {peeked_item}')
    print('Queue after dequeues:', list(queue))
if __name__ == '__main__':
    perform_queue_operations()