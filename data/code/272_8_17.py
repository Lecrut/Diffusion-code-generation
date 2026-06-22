def quick_sort(words):
    if len(words) <= 1:
        return words
    pivot = words[len(words) // 2]
    left = [word for word in words if word < pivot]
    middle = [word for word in words if word == pivot]
    right = [word for word in words if word > pivot]
    return quick_sort(left) + middle + quick_sort(right)

if __name__ == '__main__':
    sample_words = ["banana", "apple", "cherry", "date", "elderberry"]
    sorted_words = quick_sort(sample_words)
    print("Sorted list of words:")
    for word in sorted_words:
        print(word)