from collections import deque

DEFAULT_EMPTY_RESULT = None

def extract_first(dq):
    if len(dq) == 0:
        return DEFAULT_EMPTY_RESULT
    return dq[0]

if __name__ == '__main__':
    data = deque([42, 17, 99])
    first = extract_first(data)
    print(first)