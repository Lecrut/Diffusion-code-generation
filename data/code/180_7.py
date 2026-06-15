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
    result = set_word_check(target_word, word_set)
    end_time = time.perf_counter()
    print(f"Set Size: {len(word_set)}")
    print(f"Result: {result}")
    print(f"Time taken (Set creation + Check): {(end_time - start_time) * 1000:.6f} ms")