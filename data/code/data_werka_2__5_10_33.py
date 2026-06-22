def length_difference(a, b):
    if a > b:
        return a - b
    else:
        return b - a

if __name__ == '__main__':
    first_length = 12
    second_length = 7
    difference = length_difference(first_length, second_length)
    print(difference)