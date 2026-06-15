if __name__ == '__main__':
    sequence = ['A', 'B', 'C']
    num_repeats = 50
    for i in range(num_repeats):
        output = ""
        for char in sequence:
            output += char + ", "
        print(output[:-2])