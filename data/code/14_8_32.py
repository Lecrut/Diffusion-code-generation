def compare_volumes(file_path):
    try:
        with open(file_path, 'r') as file:
            volumes = [float(line.strip()) for line in file.readlines()]
            if len(volumes) != 2:
                raise ValueError('The file must contain exactly two volume measurements.')
            return max(volumes)
    except FileNotFoundError:
        print('Error: The file was not found.')
        return None
    except ValueError as ve:
        print(f'ValueError: {ve}')
        return None
    except Exception as e:
        print(f'An unexpected error occurred: {e}')
        return None
if __name__ == '__main__':
    sample_content = '10.5\n20.3'
    with open('volumes.txt', 'w') as file:
        file.write(sample_content)
    larger_volume = compare_volumes('volumes.txt')
    if larger_volume is not None:
        print(larger_volume)