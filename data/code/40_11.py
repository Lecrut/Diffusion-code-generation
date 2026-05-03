def get_first_letters(list_of_strings):
    return [s[0] for s in list_of_strings]
if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry", "date"]
    result = get_first_letters(sample_list)
    print(result)