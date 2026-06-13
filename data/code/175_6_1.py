import re
import time
def separate_words_efficient(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return words
if __name__ == '__main__':
    large_text = "This is a large block of text designed to test the efficiency of word separation algorithms. Words are separated by spaces and punctuation marks like commas, periods, and hyphens. Efficiency is key when processing large volumes of data quickly."
    start_time = time.perf_counter()
    word_list = separate_words_efficient(large_text)
    end_time = time.perf_counter()
    print(f"Original Text Length: {len(large_text)}")
    print(f"Separated Words Count: {len(word_list)}")
    print(f"Execution Time: {(end_time - start_time) * 1000:.4f} ms")
    print("Words found:")
    print(word_list)