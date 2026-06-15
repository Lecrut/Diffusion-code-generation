import time
def set_word_check(word: str, word_set: set) -> bool:
    return word in word_set
if __name__ == '__main__':
    large_word_collection = {"apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon", "mango", "nectarine", "orange", "papaya", "pear", "quince", "raspberry", "strawberry", "tangerine", "ugle", "watermelon", "xigua", "yam"}
    word_to_check = "grape"
    start_time = time.perf_counter()
    result = set_word_check(word_to_check, large_word_collection)
    end_time = time.perf_counter()
    print(f"Word to check: {word_to_check}")
    print(f"Set size: {len(large_word_collection)}")
    print(f"Result: {result}")
    print(f"Time taken: {(end_time - start_time) * 1e6:.3f} microseconds")
    word_to_check_missing = "melon"
    start_time = time.perf_counter()
    result_missing = set_word_check(word_to_check_missing, large_word_collection)
    end_time = time.perf_counter()
    print(f"\nWord to check: {word_to_check_missing}")
    print(f"Result: {result_missing}")
    print(f"Time taken: {(end_time - start_time) * 1e6:.3f} microseconds")