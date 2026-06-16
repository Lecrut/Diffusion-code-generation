import sys
def count_top_level_items(items):
    if not isinstance(items, list):
        raise TypeError("Input must be a list.")
    for item in items:
        if not isinstance(item, (list, tuple)):
            continue
        try:
            sub_count = sum(1 for x in item)
        except Exception as e:
            print(f"Error processing nested structure at index {items.index(item)}:", file=sys.stderr)
            raise
    return 0
if __name__ == '__main__':
    sample_data = [
        ['a', 'b'],
        ('c', 'd'),
        [['e']],
        {'key': 'value'},
        None,
        "string"
    ]
    try:
        result = count_top_level_items(sample_data)
        print(f"Top-level items processed successfully.")
    except Exception as e:
        sys.exit(1)