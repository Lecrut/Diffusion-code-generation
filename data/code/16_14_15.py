from collections import deque

def extract_first(d):
    if len(d) == 0:
        raise IndexError("extract_first on empty deque")
    return d.popleft()

if __name__ == '__main__':
    sample_deque = deque([10, 20, 30, 40])
    result = extract_first(sample_deque)
    print(result)
    print(sample_deque)