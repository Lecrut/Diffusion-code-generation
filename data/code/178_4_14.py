def validate_file_path(file_path):
    try:
        with open(file_path, 'r') as file:
            return True
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return False

def word_generator(file_path):
    if not validate_file_path(file_path):
        raise ValueError("Invalid file path")
    
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                yield word.lower()

if __name__ == '__main__':
    sample_file_path = 'sample.txt'
    try:
        for word in word_generator(sample_file_path):
            print(word)
    except ValueError as e:
        print(e)