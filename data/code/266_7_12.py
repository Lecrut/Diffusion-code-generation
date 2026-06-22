from collections import Counter

def top_n_words(file_path, n):
    with open(file_path, 'r') as file:
        words = file.read().lower().split()
        word_counts = Counter(words)
        return word_counts.most_common(n)

if __name__ == '__main__':
    sample_file_path = 'sample.txt'
    top_n = 5
    print(top_n_words(sample_file_path, top_n))