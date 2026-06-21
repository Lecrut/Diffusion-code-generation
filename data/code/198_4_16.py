import operator

def find_smallest_in_list(data_list):
    if not data_list:
        raise ValueError("Input list cannot be empty.")
    smallest = min(data_list, key=operator.itemgetter(0))
    return smallest

if __name__ == '__main__':
    sample_lists = [
        [3.14, 1.618, 2.718, 0.5],
        [10, -5, 20, 3],
        [100.5, 99.9, 100.0],
        [-10, -50, 0, 1]
    ]
    
    for lst in sample_lists:
        print(f"List: {lst}")
        print(f"Smallest in List: {find_smallest_in_list(lst)}")
        print("-" * 20)