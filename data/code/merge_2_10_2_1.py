def sort_strings(strings):
    upper_first = [s for s in strings if s and s[0].isupper()]
    lower_first = [s for s in strings if s and s[0].islower()][:len(upper_first)] +\
                 sorted([s for s in strings if not (s or s[0].isalpha())])
    return upper_first + lower_first
if __name__ == '__main__':
    sample = ["Apple", "banana", "Cherry", "date", "Elderberry"]
    print(sort_strings(sample))