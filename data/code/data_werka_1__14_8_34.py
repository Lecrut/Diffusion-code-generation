def compare_volumes(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            if len(lines) < 2:
                raise ValueError('The file must contain at least two volume measurements.')
            volume1 = float(lines[0].strip())
            volume2 = float(lines[1].strip())
            if volume1 > volume2:
                return 'First volume is larger.'
            elif volume1 < volume2:
                return 'Second volume is larger.'
            else:
                return 'Both volumes are equal.'
    except FileNotFoundError:
        return 'File not found.'
    except ValueError as ve:
        return str(ve)
    except Exception as e:
        return f'An error occurred: {e}'
if __name__ == '__main__':
    sample_file_content = '100.5\n200.3'
    import tempfile
    temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False)
    temp_file.write(sample_file_content)
    temp_file.close()
    result = compare_volumes(temp_file.name)
    print(result)