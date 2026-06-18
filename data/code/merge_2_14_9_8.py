import timeit
def remove_duplicates_optimized(data):
    seen = set()
    return [x for x in data if not (x in seen or seen.add(x))]
if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] * 10 + list(range(100))
    result_list = remove_duplicates_optimized(sample_data)
    print(f"Processed {len(result_list)} unique items from original data.")