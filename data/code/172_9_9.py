def initialize_dictionary():
    words = ["one", "two", "three", "four", "five"]
    dictionary = {}
    for i in range(1, 6):
        dictionary[i] = words[i-1]
    return dictionary

if __name__ == '__main__':
    result = initialize_dictionary()
    print(result)