import re
import time
def compare_parsing_methods(text_block):
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
        return result_split, time_split
    else:
        return result_regex, time_regex
if __name__ == '__main__':
    large_text = "this is a test string with various amounts of whitespace separating the words and some extra spaces" * 100000
    print("Starting benchmark...")
    result, time_taken = compare_parsing_methods(large_text)
    print(f"Parsing completed in {time_taken:.6f} seconds.")
    print("Result (from faster method):", result)