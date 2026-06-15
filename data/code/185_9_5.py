import re
import time
def benchmark_parsing_methods(text_block):
    def parse_split(text):
        return text.split()
    def parse_regex(text):
        return re.findall(r'\S+', text)
    start_time = time.perf_counter()
    result_split = parse_split(text_block)
    time_split = time.perf_counter() - start_time
    start_time = time.perf_counter()
    result_regex = parse_regex(text_block)
    time_regex = time.perf_counter() - start_time
    if time_split < time_regex:
        return result_split, time_split, time_regex
    else:
        return result_regex, time_regex, time_split
if __name__ == '__main__':
    large_text = "this is a test string with varying amounts of whitespace separating the words and some extra spaces to test the robustness of both parsing techniques for large blocks of text" * 10000
    print(f"Benchmarking parsing methods on text length: {len(large_text)}")
    result, time_split, time_regex = benchmark_parsing_methods(large_text)
    print(f"Result found (method based on speed): {result}")
    print(f"Time taken by split method: {time_split:.6f} seconds")
    print(f"Time taken by regex method: {time_regex:.6f} seconds")