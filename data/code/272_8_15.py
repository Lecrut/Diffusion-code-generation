def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

if __name__ == '__main__':
    word_sequence = ["banana", "apple", "cherry", "date", "elderberry"]
    print("Original sequence:", word_sequence)
    sorted_words = quicksort(word_sequence)
    print("Sorted sequence:", sorted_words)