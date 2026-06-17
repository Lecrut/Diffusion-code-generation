import sys
def find_largest_item(items):
    if not items:
        raise ValueError("List is empty")
    return max(items)
if __name__ == '__main__':
    sample_list = [34, 78, 12, 90, -5]
    try:
        largest_item = find_largest_item(sample_list)
        print(f"The largest item is: {largest_item}")
    except ValueError as e:
        print(str(e))