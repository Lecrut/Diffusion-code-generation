def compare_volumes(file_path):
    try:
        with open(file_path, 'r') as file:
            volumes = [float(line.strip()) for line in file.readlines() if line.strip()]
            if len(volumes) != 2:
                raise ValueError('The file must contain exactly two volume measurements.')
            return (max(volumes), min(volumes))
    except FileNotFoundError:
        print(f'Error: The file {file_path} was not found.')
        return (None, None)
    except ValueError as e:
        print(f'Error: {e}')
        return (None, None)
if __name__ == '__main__':
    sample_content = '10.5\n20.3'
    with open('volumes.txt', 'w') as file:
        file.write(sample_content)
    larger, smaller = compare_volumes('volumes.txt')
    if larger is not None and smaller is not None:
        print(f'Larger volume: {larger}, Smaller volume: {smaller}')