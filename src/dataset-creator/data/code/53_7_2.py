import sys
def count_elements(collection):
    return sum(1 for _ in collection)
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    sample_tuple = ('a', 'b', 'c')
    print(f"List count: {count_elements(sample_list)}")
    print(f"Tuple count: {count_elements(sample_tuple)}")