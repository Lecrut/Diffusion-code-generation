def find_print_index(text: str) -> int:
    return text.lower().find("print")
if __name__ == '__main__':
    sample_text = "I want to print a message."
    result = find_print_index(sample_text)
    if result != -1:
        print(f"Target found at index {result}")