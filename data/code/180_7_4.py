import time
def set_word_check(word: str, word_set: set) -> bool:
    return word in word_set
if __name__ == '__main__':
    collection = ["apple", "banana", "cherry", "date", "elderberry", "fig"]
    target_word = "cherry"
    print(f"Original List Size: {len(collection)}")
    start_time = time.time()
    word_set = set(collection)
    check_start_time = time.time()
    result = set_word_check(target_word, word_set)
    check_end_time = time.time()
    print(f"Target Word: {target_word}")
    print(f"Result (Set Check): {result}")
    print(f"Time taken for Set Lookup: {check_end_time - check_start_time:.6f} seconds")
    large_collection = [f"word_{i}" for i in range(100000)]
    target_word_large = "word_50000"
    print("\n--- Testing with Large Dataset ---")
    start_time_large = time.time()
    large_set = set(large_collection)
    check_start_time_large = time.time()
    result_large = set_word_check(target_word_large, large_set)
    check_end_time_large = time.time()
    print(f"Large Collection Size: {len(large_collection)}")
    print(f"Target Word: {target_word_large}")
    print(f"Result (Set Check): {result_large}")
    print(f"Time taken for Set Lookup on Large Data: {check_end_time_large - check_start_time_large:.6f} seconds")