def validate_indices(phrase, indices):
    valid_indices = []
    invalid_indices = []
    for index in indices:
        if 0 <= index < len(phrase):
            valid_indices.append(index)
        else:
            invalid_indices.append(index)
    return valid_indices, invalid_indices

def extract_substrings(phrase, valid_indices):
    extracted_substrings = [phrase[index:index+1] for index in valid_indices]
    return extracted_substrings

if __name__ == '__main__':
    sample_phrase = "HelloWorld"
    sample_indices = [0, 5, 10, -1, 3]
    
    print(f"Phrase: {sample_phrase}")
    print(f"Indices to check: {sample_indices}")
    
    valid_indices, invalid_indices = validate_indices(sample_phrase, sample_indices)
    
    if invalid_indices:
        print("Invalid indices:", invalid_indices)
    
    results = extract_substrings(sample_phrase, valid_indices)
    
    for sub in results:
        print(sub)