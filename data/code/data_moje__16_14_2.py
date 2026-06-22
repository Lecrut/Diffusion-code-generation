from collections import deque

def get_first_element(d: deque):
    return d.popleft()

if __name__ == '__main__':
    sample_deque = deque([1, 2, 3])
    result = get_first_element(sample_deque)
    print(result)