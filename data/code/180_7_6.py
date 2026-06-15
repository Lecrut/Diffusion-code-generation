import time
def set_word_check(word: str, word_set: set) -> bool:
    return word in word_set
if __name__ == '__main__':
    collection = ["apple", "banana", "cherry", "date", "elderberry", "fig"]
    target_word = "cherry"
    print(f"Original List Size: {len(collection)}")
    print(f"Target Word: {target_word}")
    start_time = time.perf_counter()
    word_set = set(collection)
    end_time = time.perf_counter()
    print(f"Time for Set Creation: {end_time - start_time:.6f} seconds")
    start_time = time.perf_counter()
    result = set_word_check(target_word, word_set)
    end_time = time.perf_counter()
    print(f"Time for Set Lookup: {end_time - start_time:.6f} seconds")
    print(f"Does '{target_word}' exist in the collection? {result}")
    target_word_not_present = "grape"
    start_time = time.perf_counter()
    result_not_present = set_word_check(target_word_not_present, word_set)
    end_time = time.perf_counter()
    print(f"Does '{target_word_not_present}' exist in the collection? {result_not_present}")