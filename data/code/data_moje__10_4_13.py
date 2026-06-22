from collections import deque

def get_leftmost_item():
    dq = deque([10, 20, 30, 40, 50])
    return dq[0]

if __name__ == '__main__':
    result = get_leftmost_item()
    print(result)