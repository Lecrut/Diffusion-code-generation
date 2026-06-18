import sys
item_dict = {}
input_data = [
    "apple",
    "banana",
    123,
    "cherry",
    None,
    "date"
]
for line in input_data:
    if isinstance(line, str):
        item_dict[line] = True
    else:
        print(f"Skipping invalid input: {line}", file=sys.stderr)
if __name__ == '__main__':
    pass