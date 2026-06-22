import random

def generate_random_words(num_words):
    words = [
        "apple", "banana", "cherry", "date",
        "zebra", "ant", "bear", "cat",
        "hello", "world", "python", "java"
    ]
    return [random.choice(words) for _ in range(num_words)]

def alphabetical_sort(string_iterable):
    return sorted(list(string_iterable))

if __name__ == '__main__':
    sample1 = generate_random_words(4)
    result1 = alphabetical_sort(sample1)
    print(f"Sample 1 Input: {sample1}")
    print(f"Sample 1 Output: {result1}")

    sample2 = generate_random_words(5)
    result2 = alphabetical_sort(sample2)
    print(f"Sample 2 Input: {sample2}")
    print(f"Sample 2 Output: {result2}")

    sample3 = generate_random_words(3)
    result3 = alphabetical_sort(sample3)
    print(f"Sample 3 Input: {sample3}")
    print(f"Sample 3 Output: {result3}")