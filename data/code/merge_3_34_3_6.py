import re

def capitalize_sentences(sentence: str) -> list[str]:
    """
    Splits a sentence into words, capitalizes each word's first letter,
    and reconstructs it as a new sentence with sentences separated by periods if present.
    
    Args:
        sentence (str): The input text to process.
        
    Returns:
        list[str]: A list of processed sentences where only the initial letter is capitalized.
    """
    # Split into potential words based on spaces, handling multiple punctuation at end-of-word
    
    def capitalize_word(word):
        if not word.strip():
            return ''
        cleaned = re.sub(r'[^\w\s]', '', word)  # Remove non-alphanumeric characters except space
        if len(cleaned) == 0:
            return ' '.join(word.split()) 
        capitalized = [cleaned[0].upper(), ''.join(cleaned[i] for i in range(1, len(cleaned)))]
        return "".join(capitalized).lower() # Ensure rest are lower case

    words = sentence.strip().split(' ')
    processed_words = []
    
    if not words:
        return ['']

    current_sentence_parts = [words[0]]
    
    for i in range(1, len(words)):
        word = words[i]
        cleaned_word = re.sub(r'[^\w\s]', '', ' '.join(word.split()))
        
        # Determine if this is a new sentence (starts with uppercase or after period)
        if re.match(r'^(?<=[.!?])(?=\s*[a-zA-Z])', word): 
            current_sentence_parts.append(capitalize_word(''.join(cleaned_word.split())))
            
        else:
            cleaned_words_list = [w for w in ' '.join(word.split()).split() if w] # Filter empty strings
            
            # Capitalize first letter of each segment (word) within the sentence block logic is tricky, 
            # so let's simplify to just capitalizing every word individually as per standard title case but preserving original casing for non-first letters
            processed_parts = []
            part_str = ' '.join(cleaned_words_list).split(' ')
            
            if not cleaned_word.strip(): continue
            
            temp_capitalize_list = [w[0].upper() + w[1:] if len(w) > 1 else w.upper() for w in clean]

    return current_sentence_parts

def main():
    sample_input = "hello world, this is a test sentence. python code works great!"

    result_sentences = capitalize_sentences(sample_input.lower())
    
    print(result_sentences[0]) # Print just the first processed sentence to match simple expected output style or join them if multiple needed
    
if __name__ == '__main__':
    main()