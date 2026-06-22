def compare_temperatures(file_path):
    with open(file_path, 'r') as file:
        temp1 = float(file.readline().strip())
        temp2 = float(file.readline().strip())
    discrepancy = abs(temp1 - temp2)
    return discrepancy > 5
if __name__ == '__main__':
    sample_file_content = '20.5\n27.3'
    import tempfile
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.write(sample_file_content)
        temp_file_path = temp_file.name
    result = compare_temperatures(temp_file_path)
    print(result)