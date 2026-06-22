def count_words(text):
    words = text.split()
    return len(words)

if __name__ == '__main__':
    sample_file_path = "sample.txt"
    try:
        with open(sample_file_path, 'r') as file:
            content = file.read()
            word_count = count_words(content)
            print(f"The total number of words in '{sample_file_path}' is: {word_count}")
    except FileNotFoundError:
        print(f"File '{sample_file_path}' not found.")