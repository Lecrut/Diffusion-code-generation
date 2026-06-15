import re
import time
def benchmark_parsing(text, method_name):
    start_time = time.perf_counter()
    if method_name == "split":
        parts = text.split()
    elif method_name == "regex":
        parts = re.findall(r'\S+', text)
    else:
        raise ValueError("Unknown method")
    end_time = time.perf_counter()
    return parts, (end_time - start_time)
if __name__ == '__main__':
    large_text = "this is a test string with varying amounts of whitespace and multiple words" * 10000
    num_runs = 10
    split_results = []
    regex_results = []
    for _ in range(num_runs):
        split_res, split_time = benchmark_parsing(large_text, "split")
        regex_res, regex_time = benchmark_parsing(large_text, "regex")
        split_results.append((split_res, split_time))
        regex_results.append((regex_res, regex_time))
    avg_split_time = sum(t[1] for t in split_results) / num_runs
    avg_regex_time = sum(t[1] for t in regex_results) / num_runs
    print(f"Average Split Time: {avg_split_time:.6f} seconds")
    print(f"Average Regex Time: {avg_regex_time:.6f} seconds")
    if avg_split_time < avg_regex_time:
        print("Split method was more performant.")
    elif avg_regex_time < avg_split_time:
        print("Regex method was more performant.")
    else:
        print("Both methods had approximately equal performance.")