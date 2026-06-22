from collections import deque

def extract_first_element(d):
    if not d:
        raise IndexError("Cannot extract from an empty deque")
    return d.popleft()

if __name__ == '__main__':
    sample_deque = deque([1, 2, 3, 4, 5])
    result = extract_first_element(sample_deque)
    print(result)