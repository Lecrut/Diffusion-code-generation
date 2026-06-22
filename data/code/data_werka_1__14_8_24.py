def compare_volumes(file_path):
    try:
        with open(file_path, 'r') as file:
            volumes = [float(line.strip()) for line in file if line.strip()]
            if len(volumes) != 2:
                raise ValueError('The file must contain exactly two volume measurements.')
            return max(volumes)
    except FileNotFoundError:
        print('Error: The file was not found.')
    except ValueError as ve:
        print(f'ValueError: {ve}')
    except Exception as e:
        print(f'An unexpected error occurred: {e}')
if __name__ == '__main__':
    sample_volumes = '10.5\n20.3'
    import tempfile
    with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp_file:
        temp_file.write(sample_volumes)
        temp_file_path = temp_file.name
    larger_volume = compare_volumes(temp_file_path)
    if larger_volume is not None:
        print(larger_volume)