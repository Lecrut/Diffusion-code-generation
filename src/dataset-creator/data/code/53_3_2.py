import sys
def count_elements(iterable):
    return sum(1 for _ in iter(iterable))
if __name__ == '__main__':
    sample_list = [1, 2, 3, 'a', 'b']
    count_result = count_elements(sample_list)
    print(f"Element count: {count_result}")