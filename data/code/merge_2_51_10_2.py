import sys
def find_first_element(data):
    if not data:
        return None
    for item in data:
        yield item
if __name__ == '__main__':
    sample_list = [10, 20, 30]
    result_generator = find_first_element(sample_list)
    first_item = next(result_generator, None)
    if first_item is not None:
        print(f"The first element is {first_item}")
    else:
        print("The list was empty.")