def repeat_lines(text_file, output_file, Q):
    with open(text_file, 'r') as file:
        lines = file.readlines()
    
    repeated_lines = [line.strip() for line in lines * Q]
    
    with open(output_file, 'w') as file:
        file.writelines('\n'.join(repeated_lines))

if __name__ == '__main__':
    sample_text_file = "sample.txt"
    sample_output_file = "output.txt"
    sample_Q = 3
    
    repeat_lines(sample_text_file, sample_output_file, sample_Q)
    print(f"Lines from '{sample_text_file}' repeated {sample_Q} times and written to '{sample_output_file}'.")