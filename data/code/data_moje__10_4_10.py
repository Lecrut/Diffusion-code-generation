from collections import deque

def extract_front_element(initial_items):
    buffer = deque(initial_items)
    head_value = buffer[0]
    return head_value

if __name__ == '__main__':
    test_sequence = [100, 200, 300, 400, 500]
    output = extract_front_element(test_sequence)
    print(output)