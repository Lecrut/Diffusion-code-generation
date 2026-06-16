import random
def sort_large_dataset(data):
    return sorted(data)
if __name__ == '__main__':
    sample_data = [random.randint(-10**6, 10**6) for _ in range(5000)] +\
                  [round(random.uniform(-10**4.5, 10**4.5), 2) for _ in range(3000)]
    sorted_data = sort_large_dataset(sample_data)
    print(f"Original size: {len(sample_data)}")
    print("First 5 elements:", sample_data[:5])
    print("Sorted first 5 elements:", sorted_data[:5])