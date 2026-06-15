import time
def set_word_check(word: str, word_set: set) -> bool:
    return word in word_set
if __name__ == '__main__':
    large_word_collection = {"apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon", "mango"}
    target_word_present = "banana"
    target_word_absent = "watermelon"
    print("--- Checking for existing words in a Set ---")
    start_time = time.perf_counter()
    result1 = set_word_check(target_word_present, large_word_collection)
    end_time1 = time.perf_counter()
    print(f"Checking '{target_word_present}': {result1}")
    print(f"Time taken: {(end_time1 - start_time) * 1e6:.3f} microseconds")
    start_time = time.perf_counter()
    result2 = set_word_check(target_word_absent, large_word_collection)
    end_time2 = time.perf_counter()
    print(f"Checking '{target_word_absent}': {result2}")
    print(f"Time taken: {(end_time2 - start_time) * 1e6:.3f} microseconds")