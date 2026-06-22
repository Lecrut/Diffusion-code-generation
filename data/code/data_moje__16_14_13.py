from collections import deque

def extract_first(deque_obj):
    return deque_obj.popleft()

if __name__ == '__main__':
    d = deque([1, 2, 3])
    result = extract_first(d)
    print(result)