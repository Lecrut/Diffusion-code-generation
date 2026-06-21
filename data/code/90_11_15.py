def contains_a_or_b_prefix(words):
    if not isinstance(words, list):
        raise ValueError("Input must be a list")
    
    valid_starters = set(['A', 'B'])
    
    for word in words:
        if not isinstance(word, str):
            raise ValueError("List elements must be strings")
        if len(word) > 0 and word[0] in valid_starters:
            return True
            
    return False

if __name__ == '__main__':
    input_list = ['Apple', 'Banana', 'Cherry']
    outcome = contains_a_or_b_prefix(input_list)
    print(outcome)