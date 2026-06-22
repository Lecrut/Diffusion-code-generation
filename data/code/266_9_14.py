import re

def count_word_lengths(file_path):
    word_length_counts = {}
    
    with open(file_path, 'r') as file:
        for line in file:
            words = re.findall(r'\b\w+\b', line)
            for word in words:
                length = len(word)
                if length not in word_length_counts:
                    word_length_counts[length] = 0
                word_length_counts[length] += 1
    
    return word_length_counts

if __name__ == '__main__':
    sample_file_path = 'sample.txt'
    print(count_word_lengths(sample_file_path))