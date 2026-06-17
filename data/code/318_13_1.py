import logging
logging.basicConfig(level=logging.WARNING, format='%(levelname)s: %(message)s')
def compare_adjacent(data):
    n = len(data)
    for i in range(n - 1):
        val1 = data[i]
        val2 = data[i+1]
        try:
            if val1 != val2:
                logging.warning(f"Comparison failed at index {i}: {val1} != {val2}")
        except TypeError as e:
            logging.error(f"Type error during comparison at index {i}: {e}. Values were {val1} and {val2}")
if __name__ == '__main__':
    sample_data = [1, 2, "a", 4, "b", 6]
    print("--- Testing Comparison ---")
    compare_adjacent(sample_data)
    sample_data_mixed = [10, "hello", 20, "world", 30]
    print("\n--- Testing Mixed Type Comparison ---")
    compare_adjacent(sample_data_mixed)
    sample_data_all_strings = ["apple", "banana", "cherry"]
    print("\n--- Testing All String Comparison ---")
    compare_adjacent(sample_data_all_strings)
    sample_data_error = [1, "two", 3]
    print("\n--- Testing Error Handling ---")
    compare_adjacent(sample_data_error)