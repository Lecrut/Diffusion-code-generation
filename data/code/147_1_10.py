def sort_in_place(strings):
    n = len(strings)
    for i in range(n):
        for j in range(0, n-i-1):
            if strings[j] > strings[j+1]:
                strings[j], strings[j+1] = strings[j+1], strings[j]

if __name__ == '__main__':
    sample_strings = ["banana", "apple", "cherry"]
    sort_in_place(sample_strings)
    print(sample_strings)