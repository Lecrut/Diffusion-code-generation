from collections import deque

def validate_input(action, item=None):
    if action not in ['enqueue', 'dequeue']:
        raise ValueError("Invalid action. Use 'enqueue' or 'dequeue'.")
    if action == 'enqueue' and item is None:
        raise ValueError("Item must be provided for enqueue operation.")
    if action == 'dequeue' and len(queue) == 0:
        raise ValueError("Queue is empty, cannot dequeue.")

queue = deque()

def perform_action(action, item=None):
    validate_input(action, item)
    if action == 'enqueue':
        queue.append(item)
        return f"Enqueued: {item}"
    elif action == 'dequeue':
        return f"Dequeued: {queue.popleft()}"

if __name__ == '__main__':
    print(perform_action('enqueue', 1))
    print(perform_action('enqueue', 2))
    print(perform_action('enqueue', 3))
    print(perform_action('dequeue'))
    print(perform_action('dequeue'))
    print(perform_action('dequeue'))