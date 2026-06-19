def compare_volumes(file_path):
    try:
        with open(file_path, 'r') as file:
            volumes = [float(line.strip()) for line in file.readlines()]
            if len(volumes) != 2:
                raise ValueError('The file must contain exactly two volume measurements.')
            return 'First volume is larger' if volumes[0] > volumes[1] else 'Second volume is larger'
    except FileNotFoundError:
        return 'File not found.'
    except ValueError as ve:
        return str(ve)
    except Exception as e:
        return f'An error occurred: {e}'
if __name__ == '__main__':
    sample_content = '10.5\n20.3'
    with open('volumes.txt', 'w') as file:
        file.write(sample_content)
    result = compare_volumes('volumes.txt')
    print(result)