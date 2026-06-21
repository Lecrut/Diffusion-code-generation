def convert_and_sort(strings):
    return sorted(map(int, strings))

if __name__ == '__main__':
    sample_values = ["23", "1", "45", "7", "0"]
    print(convert_and_sort(sample_values))