from collections import deque

def print_leftmost(deque_instance):
    return deque_instance[0]

if __name__ == '__main__':
    sample_deque = deque([10, 20, 30, 40, 50])
    result = print_leftmost(sample_deque)
    print(result)