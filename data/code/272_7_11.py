import random

def generate_random_words(count):
    words = []
    for _ in range(count):
        word_length = random.randint(3, 10)
        word = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=word_length))
        words.append(word)
    return words

def alphabetical_sort(string_iterable):
    return sorted(list(string_iterable))

if __name__ == '__main__':
    sample_count = 5
    random_words = generate_random_words(sample_count)
    print(f"Random Words: {random_words}")
    sorted_words = alphabetical_sort(random_words)
    print(f"Sorted Words: {sorted_words}")