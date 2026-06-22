import string

def count_punctuation(file_path):
    punctuation_count = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                for char in line:
                    if char in string.punctuation:
                        punctuation_count[char] = punctuation_count.get(char, 0) + 1
    except FileNotFoundError:
        print("File not found.")
        return {}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {}
    return punctuation_count

if __name__ == '__main__':
    sample_text = "Hello, world! This is a test. It contains various punctuation marks:.,;:'\"!?()[]{}@#$%^&*-_+=|\\/<>"
    with open('sample.txt', 'w') as file:
        file.write(sample_text)
    result = count_punctuation('sample.txt')
    print(result)