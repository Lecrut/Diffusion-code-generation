import sys
def sort_large_dataset():
    data = (f"item_{i}" for i in range(10**7))
    return list(sorted(data))
if __name__ == '__main__':
    result = sort_large_dataset()
    print(f"Sorted {len(result)} items.")