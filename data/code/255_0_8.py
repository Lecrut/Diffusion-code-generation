MAX_VALUE = float('-inf')

def find_maximum(numbers):
    if not numbers:
        return None
    max_element = MAX_VALUE
    for number in numbers:
        if number > max_element:
            max_element = number
    return max_element
if __name__ == '__main__':
    sample1 = [10, 5, 20, 8]
    print(find_maximum(sample1))
    sample2 = [-5, -1, -10, -3]
    print(find_maximum(sample2))
    sample3 = [42]
    print(find_maximum(sample3))
    empty_list = []
    print(find_maximum(empty_list))