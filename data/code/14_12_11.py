def check_duplicate_characters(text):
    BOUNDARY_LENGTH = 27
    BASE_VALUE = ord('a')
    if len(text) > BOUNDARY_LENGTH:
        return True
    seen_mask = 0
    for character in text:
        offset = ord(character) - BASE_VALUE
        if (seen_mask >> offset) & 1:
            return True
        seen_mask |= (1 << offset)
    return False

if __name__ == '__main__':
    test_sequence_one = "algorithm"
    test_sequence_two = "programming"
    test_sequence_three = "code"
    test_sequence_four = "sequence"
    print(check_duplicate_characters(test_sequence_one))
    print(check_duplicate_characters(test_sequence_two))
    print(check_duplicate_characters(test_sequence_three))
    print(check_duplicate_characters(test_sequence_four))