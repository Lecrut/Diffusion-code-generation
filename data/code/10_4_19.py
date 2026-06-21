from collections import deque

def get_leftmost_element(data: deque):
    if not data:
        raise ValueError("Deque is empty")
    return data[0]

if __name__ == '__main__':
    sample_data = deque([10, 20, 30, 40])
    leftmost = get_leftmost_element(sample_data)
    print(leftmost)