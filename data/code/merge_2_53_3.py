import sys
def count_elements(iterable):
    return sum(1 for _ in iterable)
if __name__ == '__main__':
    sample_list = [10, 20, 30]
    sample_tuple = ('a', 'b')
    count_1 = count_elements(sample_list)
    count_2 = count_elements(sample_tuple)
    print(f"List length: {len(sample_list)}")
    print(f"Tuple length: {count_2}")