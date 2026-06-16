import sys
def process_items(items: list[str], binary_choice: str) -> int:
    if not items:
        return 0
    count = sum(1 for item in items if (binary_choice == 'yes' and item.startswith('a')) or 
                (binary_choice == 'no' and item.endswith('z')))
    result_list = [item + '_processed' if count > 0 else item for item in items]
    return len(result_list)
if __name__ == '__main__':
    sample_items = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    binary_choice_str = sys.argv[1] if len(sys.argv) > 1 else 'yes'
    try:
        binary_choice = binary_choice_str.lower() in ('true', 'yes')
        final_result = process_items(sample_items, str(binary_choice))
        print(final_result)
    except Exception as e:
        sys.exit(1)