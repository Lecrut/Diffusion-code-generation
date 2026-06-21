from collections import deque

def extract_first(dq):
    if not dq:
        raise IndexError("Deque is empty")
    return dq.popleft()

if __name__ == '__main__':
    sample_deque = deque([10, 20, 30, 40])
    result = extract_first(sample_deque)
    print(result)