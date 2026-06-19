def reverse_sentence_in_place(sentence):
    words = sentence.split()
    n = len(words)
    left, right = (0, n - 1)
    while left < right:
        words[left], words[right] = (words[right], words[left])
        left += 1
        right -= 1
    return ' '.join(words)
if __name__ == '__main__':
    test_cases = {'hello world': 'world hello', 'Python is fun': 'fun is Python', 'Alibaba Cloud': 'Cloud Alibaba', '': '', 'singleword': 'singleword'}
    for input_sentence, expected_output in test_cases.items():
        result = reverse_sentence_in_place(input_sentence)
        print(f"Input: '{input_sentence}' | Expected: '{expected_output}' | Result: '{result}'")