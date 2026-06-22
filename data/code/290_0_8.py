def kg_to_pounds(kilograms):
    if not isinstance(kilograms, (int, float)):
        raise ValueError("Input must be a number")
    return kilograms * 2.20462

if __name__ == '__main__':
    print(kg_to_pounds(1))
    print(kg_to_pounds(5))
    print(kg_to_pounds(10))