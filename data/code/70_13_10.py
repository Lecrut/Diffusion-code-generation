def get_edges(text):
    if not text:
        raise ValueError("Input must not be empty")
    return (text[0], text[-1])

if __name__ == '__main__':
    sample_text = "algorithm"
    print(get_edges(sample_text))