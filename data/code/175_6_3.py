import re
import time
def fast_word_separator(text):
    words = re.findall(r'\b\w+\b', text)
    return words
if __name__ == '__main__':
    large_text = "This is a sample text for benchmarking word separation. It contains various words and punctuation marks, like commas, periods, and other symbols. We want to test the efficiency of this function on a large block of text."
    num_runs = 1000
    start_time = time.perf_counter()
    for _ in range(num_runs):
        result = fast_word_separator(large_text)
    end_time = time.perf_counter()
    total_time = end_time - start_time
    average_time = total_time / num_runs
    print(f"Text length: {len(large_text)}")
    print(f"Number of runs: {num_runs}")
    print(f"Total time for {num_runs} runs: {total_time:.6f} seconds")
    print(f"Average time per run: {average_time:.9f} seconds")