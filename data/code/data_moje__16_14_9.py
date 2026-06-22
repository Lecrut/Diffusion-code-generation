from collections import deque

def extract_first_element(d: deque):
    return d.popleft()

if __name__ == '__main__':
    d = deque([10, 20, 30])
    result = extract_first_element(d)
    print(result)