from collections import deque

def get_leftmost_item(data):
    dq = deque(data)
    return dq[0]

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    result = get_leftmost_item(sample_data)
    print(result)