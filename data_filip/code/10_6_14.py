def reverse_word_order(s):
    words = s.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)

if __name__ == '__main__':
    print(reverse_word_order("hello world"))
    print(reverse_word_order("one two three"))
    print(reverse_word_order("python is fun"))