from collections import deque

def get_first_element(data_list):
    double_ended = deque(data_list)
    mapping = {0: double_ended[0]}
    return mapping[0]

if __name__ == '__main__':
    values = [100, 200, 300]
    output = get_first_element(values)
    print(output)