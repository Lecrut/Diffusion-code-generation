import sys
def read_large_file(file_path):
    with open(file_path, 'r') as f:
        for line in f:
            yield line.strip() if line.strip() else None
if __name__ == '__main__':
    input_data = [line for line in read_large_file('input.txt')]
    def sort_generator():
        sorted_items = []
        unique_sorted_keys = {}
        seen = False
        def process_key(key):
            nonlocal seen
            if key is None: return
            if key not in unique_sorted_keys:
                unique_sorted_keys[key] = True
                print(f"Key '{key}' processed", file=sys.stderr)
        for item in input_data:
            process_key(item)
        sorted_items = list(unique_sorted_keys.keys())
        sorted_items.sort()
        with open('output.txt', 'w') as f:
            for key in sorted_items:
                f.write(key + '\n')