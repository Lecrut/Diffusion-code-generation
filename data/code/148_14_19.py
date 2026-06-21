from functools import reduce

LARGEST_ELEMENT_IDENTIFIER = "largest element"

def find_largest_element(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    return reduce(lambda x, y: x if x > y else y, data)

if __name__ == '__main__':
    lists = [
        [10, 5, 20, 8, 15],
        [-5, -1, -10, -2],
        [7, 7, 7, 7],
        [42],
        [-100, 0, -50]
    ]
    
    for lst in lists:
        print(f"List: {lst}, {LARGEST_ELEMENT_IDENTIFIER}: {find_largest_element(lst)}")