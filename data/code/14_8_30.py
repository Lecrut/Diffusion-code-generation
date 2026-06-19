def compare_volumes(file_path):
    try:
        with open(file_path, 'r') as file:
            volumes = [float(line.strip()) for line in file if line.strip()]
        if len(volumes) != 2:
            raise ValueError('The file must contain exactly two volume measurements.')
        return max(volumes)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None
    except ValueError as ve:
        print(f'ValueError: {ve}')
        return None
    except Exception as e:
        print(f'An unexpected error occurred: {e}')
        return None
if __name__ == '__main__':
    sample_content = '10.5\n20.3'
    import tempfile
    temp_file = tempfile.NamedTemporaryFile(delete=False, mode='w+t')
    temp_file.write(sample_content)
    temp_file.close()
    larger_volume = compare_volumes(temp_file.name)
    if larger_volume is not None:
        print(larger_volume)