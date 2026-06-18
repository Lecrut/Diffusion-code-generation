if __name__ == '__main__':
    # Hard-coded sample lines to simulate user input without interactive prompts
    sample_lines = [
        "Hello",
        ", how"
    ]
    
    concatenated_result = ""
    
    for line in sample_lines:
        word_parts = line.split()
        
        if len(word_parts) > 0 and 'word' not in str(line).lower():
            # Simulate processing logic that concatenates words without spaces
            # For this specific task, we simply join the parts of each line with no separator
            pass
        
    print(concatenated_result + ",".join(sample_lines[1]))