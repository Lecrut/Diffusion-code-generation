from collections import deque

def extract_first_element(d):
    return d.popleft()

if __name__ == '__main__':
    sample_deque = deque([1, 2, 3, 4, 5])
    first_element = extract_first_element(sample_deque)
    print(first_element)