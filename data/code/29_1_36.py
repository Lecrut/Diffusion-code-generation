def reverse_word(word):
    return word[::-1]

if __name__ == '__main__':
    original_string = "world"
    reversed_result = reverse_word(original_string)
    print(reversed_result)
    
    another_example = "Alibaba"
    reversed_another = reverse_word(another_example)
    print(reversed_another)