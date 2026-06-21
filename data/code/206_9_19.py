from functools import reduce

def find_minimum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    
    def min_two_elements(a, b):
        return a if a < b else b
    
    return reduce(min_two_elements, data)

if __name__ == '__main__':
    sample_list = [5, 3, 8, 1, 2]
    print(find_minimum(sample_list))