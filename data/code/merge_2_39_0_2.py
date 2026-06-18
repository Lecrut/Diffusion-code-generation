import sys
def find_largest_item(items):
    if not items:
        return "Error: List is empty"
    largest = max(items)
    return f"Largest item in the list is {largest}"
if __name__ == '__main__':
    sample_list = [3, 50, -12, 89, 4]
    result = find_largest_item(sample_list)
    print(result)