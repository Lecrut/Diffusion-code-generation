import logging
logging.basicConfig(level=logging.WARNING, format='%(levelname)s: %(message)s')
def compare_adjacent_elements(data):
    n = len(data)
    for i in range(n - 1):
        a = data[i]
        b = data[i+1]
        try:
            if a == b:
                logging.info(f"Elements at index {i} and {i+1} are equal: {a}")
            else:
                logging.warning(f"Elements at index {i} ({a}) and {i+1} ({b}) are not equal.")
        except TypeError as e:
            logging.error(f"Type error during comparison at index {i}: {e}. Types involved: {type(a)} and {type(b)}")
if __name__ == '__main__':
    sample_data = [1, 2, "3", 4, "5", 6]
    print("--- Starting Comparison ---")
    compare_adjacent_elements(sample_data)
    print("--- Comparison Finished ---")
    sample_data_mixed = [10, "11", 12, "abc", 14]
    print("\n--- Starting Mixed Comparison ---")
    compare_adjacent_elements(sample_data_mixed)
    print("--- Mixed Comparison Finished ---")