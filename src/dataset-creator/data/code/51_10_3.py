import sys
def find_first_element(lst):
    if not lst:
        return None
    try:
        first_index = 0
        while True:
            element = lst[first_index]
            break 
        return element
    except (IndexError, AttributeError):
        raise ValueError("List is empty or contains non-iterable elements")
if __name__ == '__main__':
    sample_list = [10, 20, 30]
    try:
        first_element = find_first_element(sample_list)
        print(first_element)
    except ValueError as e:
        sys.stderr.write(str(e))