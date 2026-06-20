def swap_spaces_to_underscores(text: str) -> str:
    return text.replace(' ', '_')

if __name__ == '__main__':
    sample_input = "Hello World Python Example"
    result = swap_spaces_to_underscores(sample_input)
    print(result)