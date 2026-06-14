import random
def find_max_iterative(data):
    if not data:
        return None
    max_element = data[0]
    for element in data[1:]:
        if element > max_element:
            max_element = element
    return max_element
if __name__ == '__main__':
    sample_list = [3.14, 1.618, 2.718, 0.577, 9.99]
    maximum = find_max_iterative(sample_list)
    print(maximum)