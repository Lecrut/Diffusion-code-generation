from collections import deque

def get_leftmost_item(d):
    return d[0]

if __name__ == '__main__':
    sample_data = deque([10, 20, 30, 40, 50])
    result = get_leftmost_item(sample_data)
    print(result)