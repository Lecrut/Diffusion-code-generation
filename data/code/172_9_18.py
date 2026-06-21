words = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten"
}

def initialize_dict():
    result = {}
    for key, value in words.items():
        if isinstance(value, str):
            result[key] = value
    return result

if __name__ == '__main__':
    sample_dictionary = initialize_dict()
    print(sample_dictionary)