def get_first_letters(strings):
    return [s[0] for s in strings if s]

if __name__ == '__main__':
    sample_values = ["strawberry", "blueberry", "raspberry", "blackberry"]
    result = get_first_letters(sample_values)
    print(result)

    another_sample = ["watermelon", "cantaloupe", "honeydew", "musk melon"]
    more_results = get_first_letters(another_sample)
    print(more_results)