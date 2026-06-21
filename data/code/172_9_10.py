def initialize_dictionary():
    lookup = ["one", "two", "three", "four", "five"]
    dictionary = {}
    for i in range(5):
        dictionary[i] = lookup[i]
    return dictionary

if __name__ == '__main__':
    result = initialize_dictionary()
    print(result)