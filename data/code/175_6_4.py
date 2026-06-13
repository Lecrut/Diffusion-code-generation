import re
import time
def separate_words_efficient(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return words
if __name__ == '__main__':
    large_text = "This is a large block of text designed to test the efficiency of word separation algorithms. We need to ensure that this process is as fast as possible, prioritizing time efficiency over absolute simplicity in handling very large inputs. Words are separated by spaces, punctuation marks, and various other characters." * 1000
    start_time = time.perf_counter()
    word_list = separate_words_efficient(large_text)
    end_time = time.perf_counter()
    print(f"Time taken: {end_time - start_time}")
    print(f"Number of words found: {len(word_list)}")