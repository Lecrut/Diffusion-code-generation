def find_print_index(text: str, target: str) -> int:
    return text.find(target)
if __name__ == '__main__':
    sample_text = "The quick brown fox jumps over the lazy dog"
    search_target = "quick"
    if find_print_index(sample_text, search_target) != -1:
        print(f'Target "{search_target}" found at index {find_print_index(sample_text, search_target)}')
    else:
        print('Target not found.')