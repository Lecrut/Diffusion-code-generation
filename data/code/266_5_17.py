def read_files(file_paths):
    content = ""
    for file_path in file_paths:
        with open(file_path, 'r') as file:
            content += file.read()
    return content

def count_words(text):
    words = text.split()
    return len(words)

def calculate_average_word_length(file_paths):
    content = read_files(file_paths)
    total_words = count_words(content)
    total_characters = sum(len(word) for word in content.split())
    average_word_length = total_characters / total_words if total_words > 0 else 0
    return average_word_length

if __name__ == '__main__':
    sample_files = ['sample1.txt', 'sample2.txt']
    result = calculate_average_word_length(sample_files)
    print(f"Average word length across files: {result:.2f}")