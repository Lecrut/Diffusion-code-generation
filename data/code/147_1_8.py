def sort_in_place(strings):
    n = len(strings)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if strings[min_idx] > strings[j]:
                min_idx = j
        strings[i], strings[min_idx] = strings[min_idx], strings[i]

if __name__ == '__main__':
    sample_values = ["banana", "apple", "cherry"]
    sort_in_place(sample_values)
    print(sample_values)