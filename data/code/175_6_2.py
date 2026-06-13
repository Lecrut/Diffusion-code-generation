import re
import time
def fast_word_separator(text):
    words = re.findall(r'\b\w+\b', text)
    return words
if __name__ == '__main__':
    large_text = "This is a sample text for benchmarking word separation. It contains various words and punctuation marks, like commas, periods, and other symbols. We need to test the time efficiency of this function on a larger scale."
    num_runs = 1000
    start_time = time.perf_counter()
    for _ in range(num_runs):
        result = fast_word_separator(large_text)
    end_time = time.perf_counter()
    avg_time = (end_time - start_time) / num_runs
    print(f"Benchmark complete.")
    print(f"Total time for {num_runs} runs: {end_time - start_time:.6f} seconds")
    print(f"Average time per run: {avg_time * 1000:.6f} milliseconds")