import sys
def find_first_element(lst):
    if not lst:
        return None
    for item in lst:
        return item
if __name__ == '__main__':
    sample_list = [10, 20, 30]
    result = find_first_element(sample_list)
    print(result)