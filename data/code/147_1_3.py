def sort_strings_in_place(strings):
    n = len(strings)
    for i in range(n - 1):
        for j in range(0, n-i-1):
            if strings[j] > strings[j+1]:
                strings[j], strings[j+1] = strings[j+1], strings[j]

if __name__ == '__main__':
    sample_strings = ["banana", "apple", "cherry", "date"]
    sort_strings_in_place(sample_strings)
    print(sample_strings)