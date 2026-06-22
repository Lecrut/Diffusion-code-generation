def count_words(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            words = content.split()
            return len(words)
    except FileNotFoundError:
        raise ValueError("File not found.")
    except Exception as e:
        raise ValueError(f"An error occurred: {e}")

if __name__ == '__main__':
    sample_file_path = "sample.txt"
    word_count = count_words(sample_file_path)
    print(word_count)