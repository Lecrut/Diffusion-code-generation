from collections import deque

def get_leftmost_item(elements):
    dq = deque(elements)
    return dq[0]

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    result = get_leftmost_item(sample_values)
    print(result)