def reverse_word_order(s):
    return ' '.join(s.split()[::-1])

if __name__ == '__main__':
    sample_input = 'Python is awesome'
    result = reverse_word_order(sample_input)
    print(result)