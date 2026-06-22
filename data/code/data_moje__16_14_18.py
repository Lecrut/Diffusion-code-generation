from collections import deque

def extract_first(d):
    if not d:
        return None
    return d.popleft()

if __name__ == '__main__':
    sample_deque = deque([10, 20, 30])
    result = extract_first(sample_deque)
    print(result)
    print(list(sample_deque))