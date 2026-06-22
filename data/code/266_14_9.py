def count_words(file_path):
    try:
        with open(file_path, 'r') as file:
            return sum(len(line.split()) for line in file)
    except FileNotFoundError:
        print("File not found.")
        return 0

if __name__ == '__main__':
    sample_text = "This is a sample text.\nIt contains multiple lines.\nEach line has words."
    temp_file_path = 'sample.txt'
    with open(temp_file_path, 'w') as file:
        file.write(sample_text)
    result = count_words(temp_file_path)
    print(result)