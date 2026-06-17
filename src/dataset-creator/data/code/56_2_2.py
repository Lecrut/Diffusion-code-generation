def find_print_index(text: str) -> int:
    return text.lower().find("print")
if __name__ == '__main__':
    sample_text = "The function prints output to console."
    result = find_print_index(sample_text)
    print(f"Target found at index: {result}")