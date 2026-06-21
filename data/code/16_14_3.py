from collections import deque

def get_first_element(d):
    if not d:
        return None
    return d[0]

if __name__ == '__main__':
    sample_deque = deque([10, 20, 30, 40])
    first_value = get_first_element(sample_deque)
    print(first_value)