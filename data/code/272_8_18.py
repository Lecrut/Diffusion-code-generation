def quicksort(words):
    if len(words) <= 1:
        return words
    pivot = words[len(words) // 2]
    left = [word for word in words if word < pivot]
    middle = [word for word in words if word == pivot]
    right = [word for word in words if word > pivot]
    return quicksort(left) + middle + quicksort(right)

if __name__ == '__main__':
    word_sequence = ["zebra", "apple", "cherry", "date", "elderberry"]
    print("Original sequence:", word_sequence)
    sorted_words = quicksort(word_sequence)
    print("Sorted list of words:")
    for word in sorted_words:
        print(word)