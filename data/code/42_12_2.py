import sys
def process_input():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        print("")
        return
    delimiter = ","
    parts = []
    for line in input_data:
        if not line.strip():
            continue
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
    parts = []
    for item in sample_input:
        if isinstance(item, str):
            parts.append(item)
        else:
            print(f"Error: Invalid input type encountered: {type(item)}", file=sys.stderr)
            sys.exit(1)
    result = delimiter.join(parts)
    print(result)