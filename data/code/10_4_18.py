from collections import deque

def get_leftmost_item(elements):
    dq = deque(elements)
    return dq[0]

if __name__ == '__main__':
    sample_elements = [1, 2, 3, 4, 5]
    result = get_leftmost_item(sample_elements)
    print(result)