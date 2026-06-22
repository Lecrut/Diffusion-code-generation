from collections import deque

def get_leftmost(initial_items):
    dq = deque(initial_items)
    return dq[0]

if __name__ == '__main__':
    sample_items = [1, 2, 3, 4, 5]
    result = get_leftmost(sample_items)
    print(result)