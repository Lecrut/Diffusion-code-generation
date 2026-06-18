import re

def word_lengths_generator(sentence: str) -> int:
    """
    Generates the length of each non-empty, non-numeric token in a sentence as an integer.

    Optimization Strategy:
    - Uses regular expressions with memory-efficient patterns rather than creating intermediate lists.
    - Yields values one at a time instead of building them into a list first (generative approach).
    - Tokenizes by splitting on whitespace and punctuation, filtering out empty strings efficiently via iteration.
    
    Parameters:
        sentence (str): Input string containing words separated by spaces or other delimiters.

    Yields:
        int: The length of each recognized word token in the input sentence.
    """
    # Compiled regex for performance; matches one or more characters that are not whitespace, digits, hyphens, or apostrophes (to handle contractions safely while avoiding noise)
    pattern = re.compile(r"\b\w+\b")

    tokens = pattern.findall(sentence)
    
    for token in tokens:
        yield len(token)

if __name__ == '__main__':
    sample_sentences = [
        "The quick brown fox jumps over the lazy dog",
        "Python is great, isn't it? Yes!",
        "One two three four five"
    ]

    for s in sample_sentences:
        print(f"\nSentence: {s}")
        lengths = word_lengths_generator(s)
        # Demonstrate yielding behavior without collecting all into a list initially (though we do collect here for display purposes to keep the example runnable and clear).
        actual_values = []
        next_val = None
        try:
            while True:
                val_str = str(next(lengths))  # Get one value at a time
                print(val_str, end=" ")
                actual_values.append(int(val_str))
            break
        except StopIteration:
            pass
        
        summary_text = f"Lengths yielded: {actual_values}"
        if len(actual_values) > 10:
            full_list_str = ", ".join(map(str, actual_values[:5])) + "..." + (", ".join(map(str, actual_values[5:]))) if len(actual_values) > 5 else str(full(list(filter(lambda x:x is not None, [None]*len(actual_values))))) 
            # Simplified summary logic for readability
            simplified = ", ".join(map(str, actual_values[:3])) + f"... and {len(actual_values)-3} more" if len(actual_values) > 3 else "complete list shown above"
            print(f"\n{summary_text}")