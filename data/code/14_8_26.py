def compare_volumes(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        if len(lines) != 2:
            raise ValueError('The file must contain exactly two volume measurements, one per line.')
        volume1 = float(lines[0].strip())
        volume2 = float(lines[1].strip())
        if volume1 > volume2:
            return 'First volume is larger.'
        elif volume2 > volume1:
            return 'Second volume is larger.'
        else:
            return 'Both volumes are equal.'
    except FileNotFoundError:
        return 'File not found. Please check the file path.'
    except ValueError as ve:
        return str(ve)
    except Exception as e:
        return f'An unexpected error occurred: {e}'
if __name__ == '__main__':
    sample_file_content = '100.5\n200.3'
    with open('volumes.txt', 'w') as temp_file:
        temp_file.write(sample_file_content)
    result = compare_volumes('volumes.txt')
    print(result)