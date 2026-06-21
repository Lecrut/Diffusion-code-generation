def insert_hyphens(input_string):
    return '-'.join([char for char in input_string])

if __name__ == '__main__':
    sample_string = "Programming"
    result = insert_hyphens(sample_string)
    print(result)