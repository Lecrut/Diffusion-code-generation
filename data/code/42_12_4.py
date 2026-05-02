import sys
def process_input():
    data = sys.stdin.read().splitlines()
    if not data:
        print("")
        return
    delimiter = ","
    parts = []
    for line in data:
        parts.append(line.strip())
    if not parts:
        print("")
        return
    result = delimiter.join(parts)
    print(result)
if __name__ == '__main__':
    sample_input = [
        "apple",
        "banana",
        "cherry"
    ]
    delimiter = ","
    processed_parts = []
    for item in sample_input:
        if isinstance(item, str):
            processed_parts.append(item)
        else:
            sys.stderr.write(f"Error: Invalid input type encountered: {type(item)}\n")
            pass
    final_result = delimiter.join(processed_parts)
    print(final_result)