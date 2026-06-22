def is_valid_string(s):
    return isinstance(s, str)

def reverse_sentence_in_place(sentence):
    if not is_valid_string(sentence):
        raise ValueError("Input must be a string")
    
    sentence_list = list(sentence)
    left, right = 0, len(sentence_list) - 1
    
    while left < right:
        sentence_list[left], sentence_list[right] = sentence_list[right], sentence_list[left]
        left += 1
        right -= 1
    
    return ''.join(sentence_list)

if __name__ == '__main__':
    test_cases = [
        "hello",
        "Hello World",
        "Python is fun!",
        "",
        "A man a plan a canal Panama"
    ]
    
    for case in test_cases:
        reversed_case = reverse_sentence_in_place(case)
        print(reversed_case)