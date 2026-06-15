import time
def set_word_check(word: str, word_set: set) -> bool:
    return word in word_set
if __name__ == '__main__':
    collection = ["apple", "banana", "cherry", "date", "elderberry", "fig"]
    target_word = "cherry"
    print(f"Original List Size: {len(collection)}")
    start_time = time.perf_counter()
    word_set = set(collection)
    end_time = time.perf_counter()
    print(f"Set Creation Time: {end_time - start_time:.6f} seconds")
    start_time = time.perf_counter()
    result = set_word_check(target_word, word_set)
    end_time = time.perf_counter()
    print(f"Checking for '{target_word}' in the set:")
    print(f"Result: {result}")
    print(f"Lookup Time: {end_time - start_time:.6f} seconds")