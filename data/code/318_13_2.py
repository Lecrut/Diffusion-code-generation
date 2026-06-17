import logging
logging.basicConfig(level=logging.WARNING, format='%(levelname)s: %(message)s')
def compare_adjacent(data):
    n = len(data)
    for i in range(n - 1):
        a = data[i]
        b = data[i+1]
        try:
            if a < b:
                logging.warning(f"Comparison warning at index {i}: {a} < {b}")
            elif a > b:
                logging.warning(f"Comparison warning at index {i}: {a} > {b}")
        except TypeError as e:
            logging.error(f"Type error during comparison at index {i}: Cannot compare {a} and {b}. Error: {e}")
if __name__ == '__main__':
    sample_data = [10, 20, "30", 40, "50", 60]
    print("--- Starting Comparison ---")
    compare_adjacent(sample_data)
    print("--- Comparison Finished ---")