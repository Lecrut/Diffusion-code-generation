def sort_strings(strings):
    return sorted(
        strings, 
        key=lambda s: (s[0].isupper(), s) if len(s) > 0 else ('', s),
        reverse=True
    )
if __name__ == '__main__':
    sample_data = ["apple", "Banana", "cherry", "Date", "elderberry"]
    result = sort_strings(sample_data)
    print(result)