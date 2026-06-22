def compare_temperatures(file_content):
    lines = file_content.strip().split('\n')
    if len(lines) != 2:
        raise ValueError("The file must contain exactly two temperature values.")
    
    try:
        temp1 = float(lines[0])
        temp2 = float(lines[1])
    except ValueError:
        raise ValueError("Both temperature values must be valid numbers.")
    
    discrepancy = abs(temp1 - temp2)
    if discrepancy > 5:
        return f"Discrepancy of {discrepancy} degrees exceeds the threshold."
    else:
        return "Temperatures are within acceptable range."

if __name__ == '__main__':
    sample_file_content = """23.5
30.0"""
    result = compare_temperatures(sample_file_content)
    print(result)