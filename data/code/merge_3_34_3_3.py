import textwrap

def process_sentence(sentence: str) -> list[str]:
    """Process a sentence to ensure each word starts with its initial letter capitalized."""
    # Split the sentence into words and use a generator expression to capitalize each, then join back.
    return [word.capitalize() for word in textwrap.wrap(sentence)]

if __name__ == '__main__':
    sample_sentence = "hello world! this is python."
    result = process_sentence(sample_sentence)
    print(" ".join(result))