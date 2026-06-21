LOOKUP = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine'
}

def initialize_dictionary():
    return {i: LOOKUP[i] for i in range(10)}

if __name__ == '__main__':
    dictionary = initialize_dictionary()
    print(dictionary)