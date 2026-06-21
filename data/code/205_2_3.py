def sort_strings(strings):
    return sorted(strings, key=str.lower)

if __name__ == '__main__':
    sample_data = ["Banana", "apple", "Cherry", "date"]
    sorted_data = sort_strings(sample_data)
    print(sorted_data)