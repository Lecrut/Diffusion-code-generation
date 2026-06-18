reversed_string = "Hello, World!"
print(reversed_string[::-1])

if __name__ == '__main__':
    sample_input = "Python is great"
    reversed_result = "" if not isinstance(sample_input, str) else "".join(list(reversed(sample_input)))
    
    print("Original:", repr(sample_input))
    print("Reversed:", repr(reversed_result))