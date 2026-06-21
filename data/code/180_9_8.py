def check_word_in_identifiers(target, identifiers):
    if not isinstance(target, str) or not isinstance(identifiers, list):
        raise ValueError("Target must be a string and identifiers must be a list")
    
    return target in identifiers

if __name__ == '__main__':
    sample_target = "example"
    sample_identifiers = ["test", "sample", "example"]
    print(check_word_in_identifiers(sample_target, sample_identifiers))