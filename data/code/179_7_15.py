def reverse_word_order(s):
    if not isinstance(s, str) or not s:
        raise ValueError("Input must be a non-empty string")
    
    words = s.split()
    reversed_words = words[::-1]
    return " ".join(reversed_words)

if __name__ == '__main__':
    sample_string = "Data Science is fun"
    try:
        result = reverse_word_order(sample_string)
        print(result)
    except ValueError as e:
        print(e)