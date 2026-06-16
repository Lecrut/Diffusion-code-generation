import sys
def count_elements(lst):
    return len(lst)
if __name__ == '__main__':
    sample_list = [10, 20, 30, 'a', None]
    result_count = count_elements(sample_list)
    print(result_count)