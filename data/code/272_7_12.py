import random

def generate_and_sort_words(num_words):
    words = [random.choice('abcdefghijklmnopqrstuvwxyz') * 5 for _ in range(num_words)]
    words.sort()
    return words

if __name__ == '__main__':
    sorted_words = generate_and_sort_words(10)
    print(sorted_words)