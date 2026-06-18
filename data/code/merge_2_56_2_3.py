def find_print_index(text: str) -> int:
    return text.find("print")
if __name__ == '__main__':
    sample_text = "The function print is useful."
    result = find_print_index(sample_text)
    if result != -1:
        print(f"Target found at index {result}")