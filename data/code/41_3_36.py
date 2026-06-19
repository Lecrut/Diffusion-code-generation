def process_string(input_str):
    transformations = {
        'original': input_str,
        'lowercase': input_str.lower(),
        'reversed_case': input_str.swapcase()
    }
    return (transformations['original'], transformations['lowercase'], transformations['reversed_case'])

if __name__ == '__main__':
    sample = "Hello World"
    result = process_string(sample)
    print(result)