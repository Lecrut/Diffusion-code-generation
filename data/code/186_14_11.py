NUMERICAL_CHARS = set('0123456789')

def is_numerical(s):
    return all(char in NUMERICAL_CHARS for char in s)

def sort_numerical_strings(strings):
    numerical_strings = filter(is_numerical, strings)
    sorted_integers = sorted(map(int, numerical_strings))
    return sorted_integers

if __name__ == '__main__':
    sample_values = ["3", "1", "4", "1", "5", "9", "abc", "def"]
    print(sort_numerical_strings(sample_values))