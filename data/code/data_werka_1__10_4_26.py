def compare_temperatures(file_path):
    with open(file_path, 'r') as file:
        temp1 = float(file.readline().strip())
        temp2 = float(file.readline().strip())

    if abs(temp1 - temp2) > 5:
        return f"Discrepancy detected: {temp1} and {temp2}"
    else:
        return "No significant discrepancy"

if __name__ == '__main__':
    sample_file_content = """25.0
                            30.0"""
    
    with open('sample_temp.txt', 'w') as file:
        file.write(sample_file_content)
    
    result = compare_temperatures('sample_temp.txt')
    print(result)