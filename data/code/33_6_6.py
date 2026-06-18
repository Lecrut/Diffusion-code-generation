import sys

def main():
    # Simulate reading lines by using a predefined list of strings instead of input()
    sample_values = ["Hello", "World", "Python"]
    
    concatenated_result = ""
    
    # Process the sample values line by line (simulating user input)
    for word in sample_values:
        if not isinstance(word, str):
            raise TypeError("All elements must be strings.")
        
        # Check if there is a previous part to concatenate with no space
        if concatenated_result == "":
            concatenated_result = word
        else:
            # Append the new word directly without adding spaces between words
            concatenated_result += word
    
    print(concatenated_result)

if __name__ == '__main__':
    main()