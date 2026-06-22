from collections import deque

def get_leftmost_item(container):
    return container[0]

if __name__ == '__main__':
    sample_data = deque([10, 20, 30, 40, 50])
    leftmost = get_leftmost_item(sample_data)
    print(leftmost)