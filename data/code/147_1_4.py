def sort_strings_in_place(strings):
    n = len(strings)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if strings[j] < strings[min_idx]:
                min_idx = j
        strings[i], strings[min_idx] = strings[min_idx], strings[i]

if __name__ == '__main__':
    sample_strings = ["banana", "apple", "cherry"]
    sort_strings_in_place(sample_strings)
    print(sample_strings)