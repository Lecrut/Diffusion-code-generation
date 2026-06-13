import re
import time
def fast_word_splitter(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return words
if __name__ == '__main__':
    large_text = "This is a large block of text designed to test the efficiency of word separation algorithms. Words are separated by spaces, punctuation marks, and various other characters. Efficiency is key when processing large volumes of data quickly."
    start_time = time.perf_counter()
    result = fast_word_splitter(large_text)
    end_time = time.perf_counter()
    print(f"Input Text Length: {len(large_text)}")
    print(f"Result: {result}")
    print(f"Execution Time: {(end_time - start_time) * 1000:.4f} ms")