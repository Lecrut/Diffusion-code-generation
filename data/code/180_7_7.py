import time
def set_word_check(word: str, word_set: set) -> bool:
    return word in word_set
if __name__ == '__main__':
    collection = ["apple", "banana", "cherry", "date", "elderberry", "fig"]
    target_word = "cherry"
    word_set = set(collection)
    start_time = time.perf_counter()
    result = set_word_check(target_word, word_set)
    end_time = time.perf_counter()
    print(f"Target word: {target_word}")
    print(f"Word set size: {len(word_set)}")
    print(f"Result: {result}")
    print(f"Time taken: {(end_time - start_time) * 1e6:.3f} microseconds")