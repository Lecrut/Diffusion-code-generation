from collections import deque

def extract_first(d):
    return d.popleft()

if __name__ == '__main__':
    d = deque([1, 2, 3, 4, 5])
    print(extract_first(d))