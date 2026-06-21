from collections import deque

def get_leftmost_element(data):
    q = deque(data)
    return q[0]

if __name__ == '__main__':
    sample_data = [5, 10, 15, 20, 25]
    result = get_leftmost_element(sample_data)
    print(result)