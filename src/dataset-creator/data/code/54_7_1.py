import sys
def get_middle_index(iterable):
    length = sum(1 for _ in iterable)
    return (length - 1) // 2 if length % 2 == 0 else length // 2
if __name__ == '__main__':
    sample_list = [1, 2, 3]
    middle_index = get_middle_index(sample_list)
    print(middle_index)