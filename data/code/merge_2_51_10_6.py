import sys
def find_first_element(lst):
    if not lst:
        return None
    for item in lst:
        yield item
if __name__ == '__main__':
    sample_list = [10, 20, 30]
    result_generator = find_first_element(sample_list)
    first_item = next(result_generator) if result_generator else None
    print(first_item)