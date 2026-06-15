import re
import time
def compare_parsing_methods(text_block):
    def parse_by_splitting(text):
        return text.split()
    def parse_by_regex(text):
        return re.findall(r'\S+', text)
    start_time = time.perf_counter()
    result_split = parse_by_splitting(text_block)
    time_split = time.perf_counter() - start_time
    start_time = time.perf_counter()
    result_regex = parse_by_regex(text_block)
    time_regex = time.perf_counter() - start_time
    if time_split < time_regex:
        return result_split, time_split
    else:
        return result_regex, time_regex
if __name__ == '__main__':
    large_text = "this is a sample text block with varying amounts of whitespace between words and some extra spaces" * 100000
    result, time_taken = compare_parsing_methods(large_text)
    print("Parsing comparison complete.")
    print(f"Time taken for the chosen method: {time_taken:.6f} seconds")