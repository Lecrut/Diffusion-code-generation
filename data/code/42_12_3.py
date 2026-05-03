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
    result = delimiter.join(sample_input)
    print(result)