def sort_strings(strings):
    uppercase = [s for s in strings if s and s[0].isupper()]
    lowercase = [s for s in strings if s and not s[0].isupper() and not s[0].isdigit()]
    return sorted(uppercase) + sorted(lowercase, reverse=True)
if __name__ == '__main__':
    sample_data = ["Apple", "banana", "Cherry", "date", "Elderberry"]
    result = sort_strings(sample_data)
    print(result)