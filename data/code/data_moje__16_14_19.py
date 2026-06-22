from collections import deque

def extract_first(d):
    if not d:
        return None
    return d.popleft()

if __name__ == '__main__':
    sample_deque = deque([1, 2, 3, 4, 5])
    result = extract_first(sample_deque)
    print(result)