def reverse_string(s):
    return s[::-1]

if __name__ == '__main__':
    sample_strings = [
        "Greetings from Alibaba Cloud!",
        "Python is fun!",
        "Hello, World!"
    ]
    
    for original in sample_strings:
        result = reverse_string(original)
        print(f"Original: {original}, Reversed: {result}")