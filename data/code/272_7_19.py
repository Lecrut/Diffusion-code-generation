import random

def generate_random_words(num_words):
    if not isinstance(num_words, int) or num_words <= 0:
        raise ValueError("Number of words must be a positive integer")
    
    words = [f"word{i}" for i in range(1, num_words + 1)]
    random.shuffle(words)
    return words

def alphabetical_sort(string_iterable):
    if not all(isinstance(word, str) for word in string_iterable):
        raise ValueError("All elements must be strings")
    
    return sorted(list(string_iterable))

if __name__ == '__main__':
    sample_words = generate_random_words(5)
    sorted_words = alphabetical_sort(sample_words)
    print(f"Sample Input: {sample_words}")
    print(f"Sorted Output: {sorted_words}")