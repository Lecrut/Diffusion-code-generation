def repeat_lines(input_file, output_file, Q):
    try:
        with open(input_file, 'r') as infile:
            lines = infile.readlines()
        
        repeated_content = ''.join(lines * Q)
        
        with open(output_file, 'w') as outfile:
            outfile.write(repeated_content)
        
        return f"Repeated {len(lines)} lines {Q} times and saved to {output_file}"
    
    except FileNotFoundError:
        return "Input file not found"
    
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    print("--- Testing repeat_lines function ---")
    result = repeat_lines('sample.txt', 'output.txt', 3)
    print(result)