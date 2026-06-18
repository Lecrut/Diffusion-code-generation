def sort_strings(strings):
    upper_first = [s for s in strings if s and s[0].isupper()]
    lower_first = [s for s in strings if not (not s) and s[0].islower() or all(not c.isalpha() for c in s)]
    return sorted(upper_first + lower_first, key=lambda x: ('a' <= x[0] < 'z', 1 if any(c.isalpha() for c in x) else False))
if __name__ == '__main__':
    sample_data = ["apple", "Banana", "cherry", "Date", "fig"]
    sorted_result = sort_strings(sample_data)
    print(sorted_result)