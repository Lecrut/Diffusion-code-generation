from collections import deque

def get_leftmost(item_list):
    dq = deque(item_list)
    return dq[0]

if __name__ == '__main__':
    sample_items = ['apple', 'banana', 'cherry']
    result = get_leftmost(sample_items)
    print(result)