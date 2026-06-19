def get_first_letters(strings):
    first_letters = [s[0] for s in strings if s]
    return first_letters

if __name__ == '__main__':
    sample_data = ["kiwi", "mango", "orange", "grape", ""]
    result = get_first_letters(sample_data)
    print(result)