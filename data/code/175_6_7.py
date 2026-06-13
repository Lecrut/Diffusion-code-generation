import re
import time
def fast_word_splitter(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return words
if __name__ == '__main__':
    large_text = "This is a sample text for benchmarking word separation. It contains various words, including some longer ones and some shorter ones. The goal is to test the time efficiency of this function with a large block of text. Words are separated by spaces and punctuation." * 10000
    start_time = time.perf_counter()
    result = fast_word_splitter(large_text)
    end_time = time.perf_counter()
    print(f"Execution Time: {end_time - start_time:.6f} seconds")
    print(f"Number of words found: {len(result)}")