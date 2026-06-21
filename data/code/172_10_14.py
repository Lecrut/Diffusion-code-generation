def reverse_mapping(word_to_key):
    if not isinstance(word_to_key, dict):
        raise ValueError("Input must be a dictionary")
    
    reverse = {}
    for key, word in word_to_key.items():
        if not isinstance(key, int) or not isinstance(word, str):
            raise ValueError("Dictionary keys must be integers and values must be strings")
        
        if key in reverse:
            raise ValueError(f"Duplicate key {key} found in dictionary")
        
        reverse[key] = word
    
    return reverse

if __name__ == '__main__':
    sample_data = {
        1: "one",
        2: "two",
        3: "three"
    }
    result = reverse_mapping(sample_data)
    print(result)