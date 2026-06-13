import os
def find_error_lines(filepath):
    error_lines = []
    try:
        with open(filepath, 'r') as file:
            for line in file:
                if 'error' in line:
                    error_lines.append(line.strip())
    except FileNotFoundError:
        return error_lines
    return error_lines
if __name__ == '__main__':
    sample_filename = "large_text_file.txt"
    sample_content = [
        "This is a normal line.",
        "An error occurred in the system.",
        "Processing data successfully.",
        "Another error message found here.",
        "No issues detected.",
        "System error code 500."
    ]
    with open(sample_filename, 'w') as f:
        for line in sample_content:
            f.write(line + "\n")
    result = find_error_lines(sample_filename)
    print(result)
    os.remove(sample_filename)