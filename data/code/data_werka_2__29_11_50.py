def reverse_string(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    return s[::-1]

if __name__ == '__main__':
    sample_texts = [
        "Hello, World!",
        "Alibaba Cloud",
        "Python Programming"
    ]
    
    for original in sample_texts:
        try:
            reversed_text = reverse_string(original)
            print(f"Original: {original}, Reversed: {reversed_text}")
        except ValueError as e:
            print(f"Error: {e}")