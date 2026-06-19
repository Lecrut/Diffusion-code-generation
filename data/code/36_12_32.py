def reverse_order_of_words(sentence):
    words = sentence.split()
    return ' '.join(words[::-1])

if __name__ == '__main__':
    sample_sentence1 = "Hello world this is a test"
    reversed_sentence1 = reverse_order_of_words(sample_sentence1)
    print(f"Original: {sample_sentence1}, Reversed: {reversed_sentence1}")
    
    sample_sentence2 = "Python programming is fun"
    reversed_sentence2 = reverse_order_of_words(sample_sentence2)
    print(f"Original: {sample_sentence2}, Reversed: {reversed_sentence2}")
    
    sample_sentence3 = "Keep it simple"
    reversed_sentence3 = reverse_order_of_words(sample_sentence3)
    print(f"Original: {sample_sentence3}, Reversed: {reversed_sentence3}")