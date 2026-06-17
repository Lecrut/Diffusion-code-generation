import math
def find_min_max(data):
    if not data:
        return None, None
    smallest = min(data)
    largest = max(data)
    return smallest, largest
if __name__ == '__main__':
    sample_list = [42, 15, 89, 3, 77, 50]
    minimum, maximum = find_min_max(sample_list)
    print(f"The list is: {sample_list}")
    print(f"Smallest element: {minimum}")
    print(f"Largest element: {maximum}")