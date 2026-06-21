def initialize_dictionary(start, end):
    lookup = ["one", "two", "three", "four", "five"]
    result = {}
    for i in range(start, end):
        if i < len(lookup):
            result[i] = lookup[i]
    return result

if __name__ == '__main__':
    sample_dict = initialize_dictionary(0, 5)
    print(sample_dict)