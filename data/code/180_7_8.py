import time
def set_word_check(word: str, word_set: set) -> bool:
    return word in word_set
if __name__ == '__main__':
    large_word_collection = {"apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon", "mango"}
    search_word_present = "banana"
    search_word_absent = "grapefruit"
    print(f"Collection size: {len(large_word_collection)}")
    start_time = time.perf_counter()
    result_present = set_word_check(search_word_present, large_word_collection)
    end_time = time.perf_counter()
    print(f"Checking for '{search_word_present}': {result_present}")
    print(f"Time taken: {(end_time - start_time):.6f} seconds\n")
    start_time = time.perf_counter()
    result_absent = set_word_check(search_word_absent, large_word_collection)
    end_time = time.perf_counter()
    print(f"Checking for '{search_word_absent}': {result_absent}")
    print(f"Time taken: {(end_time - start_time):.6f} seconds")