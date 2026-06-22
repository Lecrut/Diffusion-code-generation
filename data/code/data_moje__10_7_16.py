def generate_numbers():
    values = [42, 99, 17, 88]
    for value in values:
        if not isinstance(value, int):
            raise TypeError("Only integers are allowed in the sequence")
        yield value

if __name__ == '__main__':
    iterator = generate_numbers()
    first_item = next(iterator)
    print(first_item)