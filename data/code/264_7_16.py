def word_length_distribution(text: str) -> dict[int, list[str]]:
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    
    words = text.split()
    distribution = {}
    
    for word in words:
        length = len(word)
        if length not in distribution:
            distribution[length] = []
        distribution[length].append(word)
    
    return distribution

if __name__ == '__main__':
    sample_text = "Hello world! This is a test, how are you?"
    result = word_length_distribution(sample_text)
    print(result)