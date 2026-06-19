def reverse_string(text):
    return text[::-1]

if __name__ == '__main__':
    sample_text1 = "hello"
    reversed_text1 = reverse_string(sample_text1)
    print(f"Original: {sample_text1}, Reversed: {reversed_text1}")
    
    sample_text2 = "world"
    reversed_text2 = reverse_string(sample_text2)
    print(f"Original: {sample_text2}, Reversed: {reversed_text2}")
    
    sample_text3 = "Python"
    reversed_text3 = reverse_string(sample_text3)
    print(f"Original: {sample_text3}, Reversed: {reversed_text3}")
    
    sample_text4 = "racecar"
    reversed_text4 = reverse_string(sample_text4)
    print(f"Original: {sample_text4}, Reversed: {reversed_text4}")