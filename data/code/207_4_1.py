import random
def find_max_iterative(data):
    if not data:
        return None
    max_element = data[0]
    for i in range(1, len(data)):
        if data[i] > max_element:
            max_element = data[i]
    return max_element
if __name__ == '__main__':
    sample_list = [3.14, 1.618, 2.718, 0.577, 4.0]
    maximum = find_max_iterative(sample_list)
    print(f"The sample list is: {sample_list}")
    print(f"The maximum element found iteratively is: {maximum}")