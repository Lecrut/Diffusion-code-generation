def reverse_word_order(text):
    words = text.split()
    reversed_words = words[::-1]
    return " ".join(reversed_words)

if __name__ == '__main__':
    result1 = reverse_word_order("hello world")
    print(result1)
    
    result2 = reverse_word_order("Python is awesome")
    print(result2)
    
    result3 = reverse_word_order("single")
    print(result3)