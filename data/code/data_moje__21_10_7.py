def validate_integers(*args):
    for val in args:
        if not isinstance(val, int):
            raise TypeError("All arguments must be integers")

def find_largest(a, b, c):
    validate_integers(a, b, c)
    largest = a
    if b > largest:
        largest = b
    if c > largest:
        largest = c
    return largest

if __name__ == '__main__':
    val_one = 45
    val_two = 12
    val_three = 99
    output = find_largest(val_one, val_two, val_three)
    print(output)