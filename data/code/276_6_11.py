def repeat_integers(input_file, S):
    with open(input_file, 'r') as file:
        numbers = [int(line.strip()) for line in file]
    repeated_numbers = [num for num in numbers for _ in range(S)]
    return repeated_numbers

if __name__ == '__main__':
    sample_input = "1\n2\n3"
    with open('sample.txt', 'w') as file:
        file.write(sample_input)
    result = repeat_integers('sample.txt', 3)
    print(result)