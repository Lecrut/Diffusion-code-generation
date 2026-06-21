from collections import deque

def extract_first_element(dq):
    return dq.popleft()

if __name__ == '__main__':
    sample_deque = deque([10, 20, 30, 40])
    first = extract_first_element(sample_deque)
    print(first)