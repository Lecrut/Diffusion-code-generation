def reverse_sentence_in_place(sentence):
    words = sentence.split()
    num_words = len(words)
    
    def swap_elements(lst, index1, index2):
        lst[index1], lst[index2] = lst[index2], lst[index1]
    
    left_index, right_index = 0, num_words - 1
    while left_index < right_index:
        swap_elements(words, left_index, right_index)
        left_index += 1
        right_index -= 1
    
    return ' '.join(words)

if __name__ == '__main__':
    test_sentence = 'Alibaba Cloud is great'
    reversed_sentence = reverse_sentence_in_place(test_sentence)
    print(reversed_sentence)