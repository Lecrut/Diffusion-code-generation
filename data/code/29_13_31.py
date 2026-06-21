def reverse_string(s):
    return ''.join(reversed(s))

if __name__ == '__main__':
    sample_values = {
        "greeting": "Hello, World!",
        "number": "12345",
        "word": "Python"
    }
    
    for key, value in sample_values.items():
        reversed_value = reverse_string(value)
        print(f"Original: {value} -> Reversed: {reversed_value}")