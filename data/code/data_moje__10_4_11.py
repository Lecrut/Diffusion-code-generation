from collections import deque

def get_leftmost_element(data):
    d = deque(data)
    return d[0]

if __name__ == '__main__':
    sample_items = [10, 20, 30, 40, 50]
    result = get_leftmost_element(sample_items)
    print(result)