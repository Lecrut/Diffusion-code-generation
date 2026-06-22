SORT_THRESHOLD = 100

def quick_sort(words):
    if len(words) <= SORT_THRESHOLD:
        return sorted(words)
    pivot = words[len(words) // 2]
    left = [word for word in words if word < pivot]
    middle = [word for word in words if word == pivot]
    right = [word for word in words if word > pivot]
    return quick_sort(left) + middle + quick_sort(right)

if __name__ == '__main__':
    word_sequence = ["banana", "apple", "cherry", "date", "elderberry"]
    sorted_words = quick_sort(word_sequence)
    print("Sorted sequence:", sorted_words)