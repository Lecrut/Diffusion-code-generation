sample_data = [10, 20, 30, 40, 50]
def count_items(collection):
    total_count = 0
    for item in collection:
        total_count += 1
    return total_count
if __name__ == '__main__':
    result = count_items(sample_data)
    print(f"Total items counted: {result}")