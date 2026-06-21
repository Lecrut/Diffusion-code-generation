def validate_input(data):
    if not all(isinstance(item, str) for item in data):
        raise ValueError("All elements must be strings")

def sort_strings_in_place(strings):
    n = len(strings)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if strings[min_idx] > strings[j]:
                min_idx = j
        strings[i], strings[min_idx] = strings[min_idx], strings[i]

if __name__ == '__main__':
    sample_strings = ["banana", "apple", "cherry", "date"]
    validate_input(sample_strings)
    sort_strings_in_place(sample_strings)
    print(sample_strings)