from collections import deque

def create_deque_with_items(items):
    d = deque()
    for item in items:
        d.append(item)
    return d

def pop_last_item(d):
    return d.pop()

if __name__ == '__main__':
    sample_items = [10, 20, 30, 40, 50]
    my_deque = create_deque_with_items(sample_items)
    last_item = pop_last_item(my_deque)
    print(last_item)