class FileReverser:
    def __init__(self):
        self.lines = []
    
    def load_lines(self, file_path):
        with open(file_path, 'r') as file:
            self.lines = file.readlines()
    
    def reverse_and_store(self, output_file_path):
        reversed_lines = self.lines[::-1]
        with open(output_file_path, 'w') as file:
            file.writelines(reversed_lines)
        return output_file_path

if __name__ == '__main__':
    reverser = FileReverser()
    sample_data = "Line 1\nLine 2\nLine 3"
    temp_file_path = 'sample.txt'
    with open(temp_file_path, 'w') as file:
        file.write(sample_data)
    
    output_file_path = reverser.reverse_and_store('reversed_sample.txt')
    print(f"Reversed lines written to {output_file_path}")