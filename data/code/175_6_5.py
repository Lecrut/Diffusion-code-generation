import re
import time
def separate_words_efficient(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return words
if __name__ == '__main__':
    sample_text = "This is a large block of text that needs to be separated efficiently for benchmarking purposes. Words are the fundamental units we seek to extract from this large body of writing."
    start_time = time.perf_counter()
    result = separate_words_efficient(sample_text)
    end_time = time.perf_counter()
    print(f"Original Text Length: {len(sample_text)}")
    print(f"Separated Words Count: {len(result)}")
    print(f"Execution Time: {(end_time - start_time) * 1000:.4f} ms")
    print("Result:", result)