def remove_spaces(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            content = file.read()
        cleaned_content = ''.join(content.split())
        with open(output_file, 'w') as file:
            file.write(cleaned_content)
    except FileNotFoundError:
        print(f"Error: The input file '{input_file}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    try:
        remove_spaces('sample.txt', 'output_no_spaces.txt')
    except Exception as e:
        print(e)