import sys
def find_largest_item(items):
    if not items:
        raise ValueError("The list is empty and cannot contain a largest item.")
    return max(items)
if __name__ == '__main__':
    sample_list = [3, 50, -12, 98, 4]
    try:
        result = find_largest_item(sample_list)
        print(f"The largest item in the list is: {result}")
    except ValueError as e:
        print(e)