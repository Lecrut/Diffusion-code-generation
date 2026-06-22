from collections import deque

def extract_first_element(dq: deque):
    return dq.popleft()

if __name__ == '__main__':
    dq = deque([1, 2, 3, 4, 5])
    result = extract_first_element(dq)
    print(result)