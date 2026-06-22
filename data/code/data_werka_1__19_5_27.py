def has_positive_number(file_path):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                try:
                    number = float(line.strip())
                    if number > 0:
                        return True
                except ValueError:
                    continue
        return False
    except IOError:
        return None

if __name__ == '__main__':
    sample_file_path = 'sample_numbers.txt'
    result = has_positive_number(sample_file_path)
    print(result)