import sys

def extract_substrings(phrase: str, indices: list[int]) -> None:
    """Extract substrings based on character indices with error handling."""
    
    # Validate phrase is not empty
    if len(phrase) == 0:
        print("Error: Phrase cannot be empty.")
        sys.exit(1)
        
    # Check each index for validity
    invalid_indices = []
    for idx in indices:
        try:
            int_val = int(idx)
            if not (-len(phrase) <= int_val < len(phrase)):
                invalid_indices.append(f"{idx} is out of bounds")
        except ValueError:
            # Handle non-integer inputs like negative numbers with decimals or letters
            pass

    if invalid_indices:
        print("Error:", " and ".join(invalid_indices))
    
    valid_substrings = []
    
    for idx in indices:
        try:
            int_idx = int(idx)
            
            # Calculate start and end positions based on inclusive index logic
            # Assuming 0-based indexing where substrings are [index, index+1]
            if -len(phrase) <= int_idx < len(phrase):
                char_at_index = phrase[int_idx]
                substring_start = max(-int(idx), min(int(len(phrase)-idx-1), len(phrase))) # Simplified length check logic
                
                # Correct approach: slice from index to next position or previous negative offset end
                if int_idx >= 0 and int_idx < len(phrase):
                    start_pos = int_idx
                    end_pos = int_idx + 2 
                    
                elif -len(phrase) <= int_idx < 0:
                    # Handle potential backward indexing (though typically not needed for standard extraction)
                    if isinstance(int_idx, str) and '-' in idx.replace('-', '')[1]: 
                        start_pos = len(phrase) + int(idx) # Convert negative to positive offset from end
                    else:
                        continue
                    
                substring_start_char = phrase[int_idx] if 0 <= int_idx < len(phrase) else ''
                
                valid_substrings.append(substring_start_char)

        except Exception as e:
            print(f"Error processing index {idx}: {e}")

    # Display results (if no errors occurred initially, or handle partial success depending on logic above)
    
def main():
    phrase = "Hello World!"
    indices = ["1", "-4", 3]

    extract_substrings(phrase, indices)

if __name__ == '__main__':
    main()