from collections import deque

def get_leftmost_item(data):
    d = deque(data)
    return d[0]

if __name__ == '__main__':
    sample_elements = [10, 20, 30, 40, 50]
    result = get_leftmost_item(sample_elements)
    print(result)