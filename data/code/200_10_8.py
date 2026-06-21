ALPHABETIC_FILTER = lambda s: all(c.isalpha() for c in s)

def filter_alphabetic(strings):
    return [s for s in strings if ALPHABETIC_FILTER(s)]

if __name__ == '__main__':
    sample_values = ["hello", "world!", "Python3", "code"]
    filtered_list = filter_alphabetic(sample_values)
    print(filtered_list)