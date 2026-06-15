if __name__ == '__main__':
    sequence = ['A', 'B', 'C']
    num_repeats = 50
    output = ""
    for i in range(num_repeats):
        for char in sequence:
            output += char + ", "
    print(output.rstrip(','))