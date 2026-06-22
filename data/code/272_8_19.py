def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

if __name__ == '__main__':
    word_sequence = ["banana", "apple", "cherry", "date", "elderberry"]
    sorted_words = quick_sort(word_sequence)
    print("Sorted list of words:")
    for word in sorted_words:
        print(word)