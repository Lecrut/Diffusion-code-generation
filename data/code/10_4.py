from collections import deque

def get_leftmost_element(elements):
    d = deque(elements)
    return d[0]

if __name__ == '__main__':
    sample_elements = [10, 20, 30, 40, 50]
    result = get_leftmost_element(sample_elements)
    print(result)