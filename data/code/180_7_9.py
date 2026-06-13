import time
def set_word_check(word: str, word_set: set) -> bool:
    return word in word_set
if __name__ == '__main__':
    collection = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
    target_word = "cherry"
    word_set = set(collection)
    start_time = time.perf_counter()
    result = set_word_check(target_word, word_set)
    end_time = time.perf_counter()
    print(f"Target word: {target_word}")
    print(f"Word set size: {len(word_set)}")
    print(f"Word found: {result}")
    print(f"Time taken: {(end_time - start_time) * 1000:.6f} ms")
    target_word_not_found = "kiwi"
    start_time = time.perf_counter()
    result_not_found = set_word_check(target_word_not_found, word_set)
    end_time = time.perf_counter()
    print(f"\nTarget word: {target_word_not_found}")
    print(f"Word found: {result_not_found}")
    print(f"Time taken: {(end_time - start_time) * 1000:.6f} ms")