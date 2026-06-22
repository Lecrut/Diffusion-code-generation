def count_words(text):
    return len(text.split())

if __name__ == '__main__':
    sample_text = "This is a sample text.\nIt contains multiple lines.\nEach line has words."
    result = count_words(sample_text)
    print(result)