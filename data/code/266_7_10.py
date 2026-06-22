import collections

NUM_WORDS = 5

def read_and_count_words(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
        words = text.split()
        word_counts = collections.Counter(words)
        most_common_words = word_counts.most_common(NUM_WORDS)
        return most_common_words

if __name__ == '__main__':
    sample_file_path = 'sample.txt'
    top_words = read_and_count_words(sample_file_path)
    print(top_words)