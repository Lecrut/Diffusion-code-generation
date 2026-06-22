def reverse_lines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    reversed_lines = lines[::-1]
    return ''.join(reversed_lines)

if __name__ == '__main__':
    sample_text = "Line 3\nLine 2\nLine 1"
    with open('temp.txt', 'w') as temp_file:
        temp_file.write(sample_text)
    
    result = reverse_lines('temp.txt')
    print(result)