from functools import reduce

def find_min(numbers):
    if not numbers:
        raise ValueError("List is empty")
    return reduce(lambda x, y: x if x < y else y, numbers)

if __name__ == '__main__':
    sample_list = [34, 15, 88, 2, 43, 15, 8, 55, 2, 19]
    result = find_min(sample_list)
    print(result)