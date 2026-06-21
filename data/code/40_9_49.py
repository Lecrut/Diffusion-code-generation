def get_first_letters(strings):
    return [s[0] for s in strings if s]

if __name__ == '__main__':
    sample_values = ["strawberry", "blueberry", "blackberry", "raspberry"]
    result = get_first_letters(sample_values)
    print(result)