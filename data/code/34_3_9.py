def capitalize_words(sentence: str) -> str:
    """
    Capitalizes the first letter of each word in a sentence using list comprehensions.
    
    Args:
        sentence (str): The input string to process.
        
    Returns:
        str: A new string with only the initial letters capitalized and spaces preserved.
    """
    # Split the sentence into words, strip whitespace from individual parts if necessary for clean processing,
    # then join them back together after capitalizing each word's first letter.
    return ' '.join(word.capitalize() if len(word) > 0 else '' 
                    for word in sentence.split())

if __name__ == '__main__':
    sample_sentence = "hello world this is a test case"
    result = capitalize_words(sample_sentence)
    print(result)