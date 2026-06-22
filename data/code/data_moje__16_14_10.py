from collections import deque

def extract_first(d):
    return d[0]

if __name__ == '__main__':
    sample_deque = deque([10, 20, 30, 40])
    result = extract_first(sample_deque)
    print(result)