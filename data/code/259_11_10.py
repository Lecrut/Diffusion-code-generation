def find_min_max(data):
    return min(data), max(data)

if __name__ == '__main__':
    sample_data = [3, 1, 4, 1, 5, 9, 2, 6]
    try:
        with open('input.txt', 'w') as input_file:
            input_file.write('\n'.join(map(str, sample_data)))
        minimum, maximum = find_min_max(sample_data)
        with open('output.txt', 'w') as output_file:
            output_file.write(f"Minimum: {minimum}\n")
            output_file.write(f"Maximum: {maximum}\n")
    except IOError as e:
        print(f"Error writing to files: {e}")