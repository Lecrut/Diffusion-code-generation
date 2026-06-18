def sort_strings(strings):
    """Sorts a list of strings alphabetically (lexicographically)."""
    return sorted(strings)

if __name__ == '__main__':
    # Sample data with mixed cases and special characters
    sample_data = ["Banana", "apple", "Cherry", "date"]
    
    # Perform sorting without case sensitivity override for standard lexicographical order as prioritized, 
    # but note that .lower() could be used if strict case-insensitivity was required.
    sorted_result = sort_strings(sample_data)
    
    print(sorted_result)