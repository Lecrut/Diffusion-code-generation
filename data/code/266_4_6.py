def count_unique_words(text):
    words = text.split()
    unique_words = set(words)
    return len(unique_words)

if __name__ == '__main__':
    sample_text = "data science is the field of study involving the extraction of knowledge from data"
    unique_count = count_unique_words(sample_text)
    print(f"The total number of unique words is: {unique_count}")