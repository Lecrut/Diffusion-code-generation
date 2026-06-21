def split_sentence(sentence):
    return sentence.split()

if __name__ == '__main__':
    test_cases = [
        ("  hello world  ", ["hello", "world"]),
        ("multiple   spaces here", ["multiple", "", "", "spaces", "here"]),
        (" leading and trailing ", ["leading", "and", "trailing"]),
        ("", [])
    ]
    
    for input_sentence, expected_output in test_cases:
        result = split_sentence(input_sentence)
        print(f"Input: '{input_sentence}'")
        print(f"Output: {result}")