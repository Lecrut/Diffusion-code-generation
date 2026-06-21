def check_word_in_identifiers(target, identifiers):
    if not isinstance(target, str) or not all(isinstance(iden, str) for iden in identifiers):
        raise ValueError("Target must be a string and identifiers must be a list of strings")
    
    return target in identifiers

if __name__ == '__main__':
    sample_target = "example"
    sample_identifiers = ["sample", "test", "example", "check"]
    print(check_word_in_identifiers(sample_target, sample_identifiers))