def is_palindrome(s):
    filtered_chars = [char.lower() for char in s if char.isalpha()]
    return filtered_chars == filtered_chars[::-1]

if __name__ == '__main__':
    sample_text_1 = "A man, a plan, a canal: Panama"
    sample_text_2 = "No 'x' in Nixon"
    
    print(is_palindrome(sample_text_1))
    print(is_palindrome(sample_text_2))