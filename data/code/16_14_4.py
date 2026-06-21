from collections import deque

def get_first_element(dq):
    return dq.popleft()

if __name__ == '__main__':
    d = deque([10, 20, 30])
    result = get_first_element(d)
    print(result)