class FileRepeater:
    DEFAULT_REPETITIONS = 3

    @staticmethod
    def repeat_lines(file_path, repetitions=DEFAULT_REPETITIONS):
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        repeated_content = ''.join(lines * repetitions)
        
        output_file_path = f"{file_path.rsplit('.', 1)[0]}_repeated.txt"
        with open(output_file_path, 'w') as output_file:
            output_file.write(repeated_content)
        
        return output_file_path

if __name__ == '__main__':
    sample_file_path = 'sample.txt'
    repeated_file_path = FileRepeater.repeat_lines(sample_file_path, 2)
    print(f"Repeated file saved to: {repeated_file_path}")