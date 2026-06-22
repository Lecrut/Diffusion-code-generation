def find_min_max(data):
    return min(data), max(data)

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 6]
    try:
        with open('input.txt', 'w') as file:
            file.write('\n'.join(map(str, sample_list)))
        minimum, maximum = find_min_max(sample_list)
        with open('output.txt', 'w') as file:
            file.write(f"Minimum: {minimum}\nMaximum: {maximum}")
        print("Results written to output.txt")
    except IOError as e:
        print(f"Error writing files: {e}")