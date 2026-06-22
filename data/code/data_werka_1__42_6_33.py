def join_strings_efficiently(strings):
    return "".join(strings)

if __name__ == '__main__':
    sample_data = {
        "greeting": ["hello", "world"],
        "language": ["python", "programming"],
        "exclamation": ["hi", "there"]
    }
    
    for key, value in sample_data.items():
        result = join_strings_efficiently(value)
        print(f"{key}: {result}")