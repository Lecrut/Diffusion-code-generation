def sort_strings(strings):
    uppercase = [s for s in strings if s and s[0].isupper()]
    lowercase = [s for s in strings if s and s[0].islower()]
    return sorted(uppercase + lowercase, key=lambda x: (x.startswith(str.upper(x)), str.lower(x)))
if __name__ == '__main__':
    sample_data = ["apple", "Banana", "cherry", "Date", "elderberry"]
    result = sort_strings(sample_data)
    print(result)