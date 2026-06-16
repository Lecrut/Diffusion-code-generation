def sort_strings(strings):
    return sorted(
        strings, 
        key=lambda s: (s[0].islower(), s) if len(s) > 0 else ('', '')
    )
if __name__ == '__main__':
    sample_data = ["apple", "Banana", "cherry", "Date", "elderberry"]
    print(sort_strings(sample_data))